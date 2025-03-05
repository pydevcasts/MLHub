import json  
import torch  
import torchaudio  
from datasets import Dataset  
from transformers import (  
    Wav2Vec2Processor, Wav2Vec2ForCTC, Wav2Vec2Config,   
    AutoFeatureExtractor, TrainingArguments, Trainer,  
    get_scheduler  
)  

# Load the Wav2Vec2 model configuration and model weights  
config = Wav2Vec2Config.from_pretrained("facebook/wav2vec2-large-960h")  
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")  
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")  
feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-large-960h")  

# Enable gradient checkpointing to save memory during training  
model.gradient_checkpointing_enable()  

# Function to load data from a JSON file  
def load_data(json_path):  
    with open(json_path, 'r', encoding='utf-8') as f:  
        data = json.load(f)  
    return Dataset.from_dict({  
        "file_path": [item["file_path"] for item in data],  
        "text": [item["text"] for item in data]  
    })  

# Function to preprocess the audio data  
def preprocess_data(batch):  
    speech_array, sampling_rate = torchaudio.load(batch["file_path"])  
    resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=16000)  
    speech_array = resampler(speech_array).squeeze().numpy()  
    audio = feature_extractor(speech_array, sampling_rate=16000, return_tensors="pt")  
    batch["input_values"] = audio["input_values"][0]  
    batch["labels"] = processor.tokenizer(batch["text"], return_tensors="pt").input_ids[0]  
    return batch  

# Load and preprocess training data  
dataset = load_data("transcript_list.json")  
dataset = dataset.map(preprocess_data, remove_columns=["file_path", "text"])  

# Load and preprocess validation data  
val_dataset = load_data("validation_transcript_list.json")  
val_dataset = val_dataset.map(preprocess_data, remove_columns=["file_path", "text"])  

# Function for collating batches of data  
def collate_fn(batch):  
    input_values = [torch.tensor(item["input_values"]) for item in batch]  
    labels = [torch.tensor(item["labels"]) for item in batch]  
    input_values = torch.nn.utils.rnn.pad_sequence(input_values, batch_first=True, padding_value=0.0)  
    labels = torch.nn.utils.rnn.pad_sequence(labels, batch_first=True, padding_value=-100)  
    return {"input_values": input_values, "labels": labels}  

# Training configuration settings  
training_args = TrainingArguments(  
    output_dir="./wav2vec2_finetuned",  
    per_device_train_batch_size=3,  # Adjusted batch size  
    gradient_accumulation_steps=2,  
    save_steps=400,  
    logging_steps=100,  
    learning_rate=1e-4,  # Updated learning rate  
    weight_decay=0.005,  
    save_total_limit=2,  
    num_train_epochs=4,  
    fp16=False,  
    push_to_hub=False,  
    eval_steps=500,  
    report_to="none",  
)  

# Move the model to CPU or GPU based on availability  
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  
model.to(device)  

# Define the optimizer  
optimizer = torch.optim.AdamW(model.parameters(), lr=training_args.learning_rate)  

# Define the learning rate scheduler  
num_training_steps = len(dataset) // training_args.per_device_train_batch_size * training_args.num_train_epochs  
scheduler = get_scheduler(  
    "linear",  
    optimizer=optimizer,  
    num_warmup_steps=int(0.1 * num_training_steps),  # 10% warmup  
    num_training_steps=num_training_steps,  
)  

# Define the Trainer for model training  
trainer = Trainer(  
    model=model,  
    eval_dataset=val_dataset,  
    args=training_args,  
    train_dataset=dataset,  
    tokenizer=processor,  
    data_collator=collate_fn,  
    optimizers=(optimizer, scheduler)  
)  

# Start the training process  
try:  
    for epoch in range(training_args.num_train_epochs):  
        trainer.train()  
        torch.cuda.empty_cache()  
        eval_results = trainer.evaluate()  
except RuntimeError as e:  
    if 'out of memory' in str(e):  
        print("Out of memory error. Consider alternatives like smaller models or CPU training.")  
        torch.cuda.empty_cache()  

# Save the trained model and processor  
model.save_pretrained("./wav2vec2_finetuned")  
processor.save_pretrained("./wav2vec2_finetuned")