import speech_recognition as sr
import pyttsx3

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"You said: {query}\n")
        return query
    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_query(query):
    if "hello" in query:
        speak("Hello! How can I assist you?")
    elif "goodbye" in query:
        speak("Goodbye! Have a nice day!")
        exit()
    else:
        speak("Sorry, I am not programmed to respond to that.")

# Main loop
while True:
    query = listen().lower()
    process_query(query)
