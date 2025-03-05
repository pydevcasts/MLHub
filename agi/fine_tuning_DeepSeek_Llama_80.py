!pip install --upgrade unsloth trl huggingface_hub

# %%capture
!pip install unsloth
!pip install --force-reinstall --no-cache-dir --no-deps git+https://github.com/unslothai/unsloth.git
!pip install --upgrade jupyter
!pip install --upgrade ipywidgets
!pip install wandb
!pip install --upgrade torch


import os  # Importing the os module to interact with the operating system

# Setting environment variables
os.environ['HUGGING_FACE_TOKEN'] = '<user_name>'  # Setting the Hugging Face token as an environment variable
os.environ['WANDB_TOKEN'] = '<username>'  # Setting the Weights & Biases token as an environment variable

# Accessing the tokens from environment variables
hugging_face_token = os.environ['HUGGING_FACE_TOKEN']  # Retrieving the Hugging Face token
wandb_token = os.environ['WANDB_TOKEN']  # Retrieving the Weights & Biases token

# Printing the tokens to verify they are set correctly
print(hugging_face_token)  # Outputting the Hugging Face token
print(wandb_token)  # Outputting the Weights & Biases token



import torch  # Importing the PyTorch library for tensor operations and deep learning models
from unsloth import FastLanguageModel  # Importing FastLanguageModel from the unsloth library
from trl import SFTTrainer  # Importing SFTTrainer for training the models
from unsloth import is_bfloat16_supported  # Importing a function to check bfloat16 support
from huggingface_hub import login  # Importing the login function from Hugging Face Hub
from transformers import TrainingArguments  # Importing TrainingArguments from the transformers library
from datasets import load_dataset  # Importing the function to load datasets
import wandb  # Importing Weights & Biases library for tracking experiments



from huggingface_hub import login  # Importing the login function from the Hugging Face Hub library

# Logging into Hugging Face account using the Hugging Face token
login(hugging_face_token)  # Using the previously defined Hugging Face token to authenticate



# Logging into Weights & Biases with the provided API key
wandb.login(key=wandb_token)  # Using the previously defined Weights & Biases token to authenticate

# Initializing a new Weights & Biases run
run = wandb.init(
    project='Fine_tune_DeepSeeek_Llama_80 for operagi',  # Specifying the project name for tracking
    job_type="training",  # Defining the type of job being run (in this case, training)
    anonymous="allow"  # Allowing anonymous access to the run (useful for public projects or testing)
)




# Setting the maximum sequence length for the model
max_seq_length = 2048  # Maximum number of tokens the model will process in a single input

# Setting the data type for model parameters (None means default data type will be used)
dtype = None  # Data type for model parameters; if None, the default type (usually float32) will be used

# Configuring the model to load in 4-bit precision
load_in_4bit = True  # Enables loading the model with 4-bit precision to reduce memory usage and speed up inference



# Loading a pre-trained language model and tokenizer
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/DeepSeek-R1-Distill-Llama-8B",  # Specifying the model name to load from Hugging Face Hub
    max_seq_length=max_seq_length,  # Setting the maximum sequence length defined earlier
    dtype=dtype,  # Specifying the data type for the model parameters; defaults to bfloat16 if using H100
    load_in_4bit=load_in_4bit,  # Configuring the model to load in 4-bit precision
    token=hugging_face_token  # Providing the Hugging Face token for authentication
)





# Updated prompt_template without the response placeholder
prompt_template = """### Introduction:
Hello, I am operagi, your knowledgeable expert here to assist you with a wide range of inquiries. I am dedicated to providing evidence-based and thoughtful responses tailored to your needs.

### Role:
You are a knowledgeable expert across diverse fields, capable of providing in-depth analysis on both general inquiries and specialized topics. Your responses should:
- Be evidence-based, drawing from credible sources and established knowledge.
- Offer a thorough exploration of options and perspectives, considering different viewpoints and contexts.
- Prioritize the safety, well-being, and ethical considerations of individuals while maintaining professional standards.
- Clearly acknowledge any limitations, uncertainties, or potential biases in your responses.
- Provide detailed explanations, incorporating relevant examples, case studies, and data where applicable to support your insights.

### Question:
{}



### Detailed Response:
<think>{}
"""  # Removed {response} placeholder

# Tokenizing the input using the modified tokenizer
inputs = tokenizer([prompt_template.format(question, "")], return_tensors="pt").to("cuda")



# Defining the question to be asked
question = """پایتخت ایران کجاست و چجور جایی است پاسخ را بصورت فارسی بنویس"""

# Preparing the model for inference
# The 'for_inference' method is used to set up the model for making predictions based on the defined question.
FastLanguageModel.for_inference(model)  # Here, 'model' is the instance of the FastLanguageModel defined earlier.




# Tokenizing the input using the tokenizer with a dummy response
dummy_response = ""  # Placeholder for response
inputs = tokenizer([prompt_template.format(question, "", dummy_response)], return_tensors="pt").to("cuda")



# Generating outputs from the model based on the tokenized inputs
outputs = model.generate(
    input_ids=inputs.input_ids,           # The input IDs generated from the tokenizer
    attention_mask=inputs.attention_mask,  # The attention mask to specify which tokens to attend to
    max_new_tokens=2000,                   # Maximum number of new tokens to generate in the output
    use_cache=True,                          # Whether to use cached key/values for faster decoding
    temperature=0.7  # تنظیم دما
)




# Decoding the generated outputs into human-readable text
response = tokenizer.batch_decode(outputs)

# Printing the portion of the response after "### Response:"
print(response[0])