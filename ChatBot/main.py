import random
import json
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import numpy as np
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents, words, classes, and the trained model
intents = json.loads(open("intents.json").read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

# Function to clean up the input sentence
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)  # Tokenize the sentence
    return [lemmatizer.lemmatize(word) for word in sentence_words]  # Lemmatize each word

# Function to create a bag of words representation
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)  # Initialize bag of words
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1  # Mark the presence of the word in the bag
    return np.array(bag)  # Return as numpy array

# Function to predict the class of the input sentence
def predict_class(sentence):
    bow = bag_of_words(sentence)  # Get bag of words
    res = model.predict(np.array([bow]))[0]  # Predict using the model
    ERROR_THRESHOLD = 0.25 
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]  # Filter results base on the class is heigher than 0.25
    results.sort(key=lambda x: x[1], reverse=True)  # Sort by probability
    return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]  # Return intents

# Function to get a response based on the predicted intents
def get_response(intents_list):
    if not intents_list:  # Check if the list is empty
        return "I'm sorry, I couldn't find any information related to that."
    
    tag = intents_list[0]['intent']  # Get the top intent
    for i in intents['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])  # Return a random response
    return ""

# Function to convert text to speech and play it
def speak(text):
    tts = gTTS(text=text, lang='en')  # Convert text to speech
    filename = "response.mp3"
    tts.save(filename)  # Save the audio file
    playsound(filename)  # Play the audio file

# Function to handle the bot's response to user input
def calling_the_bot(txt):
    predict = predict_class(txt)  # Predict the class of the input
    res = get_response(predict)  # Get the corresponding response
    speak("Found it. From our Database we found that " + res)  # Speak the response
    print("Your Symptom was: ", txt)  # Print the user's input
    print("Result found in our Database: ", res)  # Print the bot's response

# Main function to run the chatbot
if __name__ == '__main__':
    print("Bot is Running")
    recognizer = sr.Recognizer()  # Initialize the recognizer
    mic = sr.Microphone()  # Use the microphone as input
    speak("Hello user, I am Siyamak, your personal Talking Healthcare Chatbot.")  # Greet the user

    while True:
        with mic as source:
            print("Say Your Symptoms. The Bot is Listening")
            speak("You may tell me your symptoms now. I am listening")  # Prompt for symptoms
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            symp = recognizer.listen(source)  # Listen for user input
     
            try:
                text = recognizer.recognize_google(symp)  # Recognize speech
                speak("You said {}".format(text))  # Confirm what was said
                speak("Scanning our database for your symptom. Please wait.")  # Notify the user
                calling_the_bot(text)  # Process the input
            except sr.UnknownValueError:
                speak("Sorry, I could not understand your symptoms. Please try again.")  # Handle unrecognized speech
                print("Sorry, I could not understand your symptoms.")
            except sr.RequestError:
                speak("Could not request results from Google Speech Recognition service.")  # Handle request errors
                print("Could not request results from Google Speech Recognition service.")

        # Ask if the user wants to continue
        speak("If you want to continue please say Yes otherwise say exit")
        with mic as ans:
            recognizer.adjust_for_ambient_noise(ans)  # Adjust for ambient noise
            voice = recognizer.listen(ans)  # Listen for the user's response

        final = recognizer.recognize_google(voice).lower()  # Recognize the response
        if final in ['no', 'please exit', 'false']:  # Check if the user wants to exit
            speak("Thank You. Shutting Down now.")  # Thank the user
            print("Bot has been stopped by the user")  # Log the exit
            break
