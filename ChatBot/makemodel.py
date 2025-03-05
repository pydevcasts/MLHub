import random
import json
import pickle

import nltk
# Download all NLTK resources (this may take some time)
# nltk.download('all')
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,  Dropout
from tensorflow.keras.optimizers import SGD

import numpy as np

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents from the intents.json file
intents = json.loads(open("intents.json").read())

# Initialize lists to hold words, classes, and documents
words = []
classes = []
documents = []

# Define characters to ignore in the input
ignore_letters = ["?", "!", ".", ","]

# Process each intent in the intents file
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        # Tokenize each pattern and add to the word list and documents
        word_list = nltk.word_tokenize(pattern) # تقسیم متن به کلمات 
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))

        # Add the intent tag to classes if it's not already present
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

# Lemmatize words and remove ignored characters
words = [lemmatizer.lemmatize(word)
         for word in words if word not in ignore_letters]

# Sort and remove duplicates from words and classes
words = sorted(set(words))
classes = sorted(set(classes))

# Save the processed words and classes to files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Prepare the dataset for training
dataset = []
template = [0] * len(classes)  # Initialize output template

# Create the bag of words and output rows for each document
for document in documents:
    bag = []
    word_patterns = document[0] #feature
    word_patterns = [lemmatizer.lemmatize(word.lower())
                     for word in word_patterns]

    # Create a bag of words representation
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    # Create the output row for the corresponding class
    output_row = list(template)
    output_row[classes.index(document[1])] = 1 #document[1] ==>label
    dataset.append([bag, output_row])


# Shuffle the dataset to ensure randomness during training
random.shuffle(dataset)
dataset = np.array(dataset, dtype=object)

# Split the dataset into training features and labels
train_x = list(dataset[:, 0])
train_y = list(dataset[:, 1])

# Build the neural network model
model = Sequential()
model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))  # First hidden layer
model.add(Dropout(0.5))  # Dropout layer to prevent overfitting
model.add(Dense(128, activation='relu'))  # Second hidden layer
model.add(Dropout(0.5))  # Dropout layer
model.add(Dense(len(train_y[0]), activation='softmax'))  # Output layer with softmax activation

# Compile the model with SGD optimizer and categorical crossentropy loss
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model on the training data
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# Save the trained model to a file
model.save("chatbot_model.h5", hist)
print("Done!")  # Indicate that training is complete
