import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import pyaudio 
import musicLibrary 
import google.generativeai as genai
from gtts import gTTS
# import pygame
import sys
import contextlib

# Importing pygame silently to suppress unnecessary output
with contextlib.redirect_stdout(None):
    import pygame


recognizer = sr.Recognizer()

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

def speak(text):           
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    # Keep the program running until the music stops
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()       
    pygame.mixer.quit()             

def aiProcess(command):
    #  Configure API key
    genai.configure(api_key="Here_Your_API_Key") # Enter your API key

    #  Create the model instance
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")

    #  Start a chat session
    chat = model.start_chat(history=[
        {
            "role": "model",
            "parts": ["You are a virtual assistant named Jarvis developed by ShamsulHaq skilled in general tasks like Google Cloud, Gemini, Alexa etc.(give short responses and long on the user demand)"]
        }
    ])

    #  Send a user message and get response
    response = chat.send_message(command)

    #  return the response
    return(response.text)


def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        return "Opening Facebook"

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"

    elif "open whatsapp" in c:
        webbrowser.open("https://whatsapp.com")
        return "Opening WhatsApp"

    elif "open twitter" in c:
        webbrowser.open("https://twitter.com")
        return "Opening Twitter"

    elif c.startswith("play"):
        track_name = c.replace("play", "").strip()
        if track_name in musicLibrary.music:
            link = musicLibrary.music[track_name]
            webbrowser.open(link)
            return f"Playing {track_name}"
        else:
            return f"Sorry, I couldn't find the track '{track_name}'."

    elif "search google for" in c:
        query = c.replace("search google for", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searching Google for {query}"

    elif "search youtube for" in c:
        query = c.replace("search youtube for", "").strip()
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        return f"Searching YouTube for {query}"

    elif c.startswith("search"):
        query = c.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searching for {query}"

    else:
        # AI fallback
        output = aiProcess(c)
        return output
    

# Generate unique filename using timestamp
def generate_filename():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    return f"jarvis_response_{timestamp}.txt"

filename = generate_filename()

def save_response_to_file(user_command, response, filename=filename):
    with open(filename, "a", encoding="utf-8") as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] You: {user_command}\n")
        file.write(f"[{timestamp}] Jarvis: {response}\n\n")

if __name__ == "__main__":
    print("Initializing Jarvis ...") 
    speak("Initializing Jarvis ...") 

    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing...") 
        speak("recognizing...") 

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)    # handles background noise 
                print("Listening...")
                speak("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                wake_word = r.recognize_google(audio)
                print(f"You Say: {wake_word}")
            if (wake_word.lower() == "jarvis"):
                print("Yes, I am here.")
                speak("Yes, I am here.")

                # Now listening for Command
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"You said: {command}")

                    response = processCommand(command)
                    print(f"Jarvis: {response}")
                    speak(response)
                    save_response_to_file(command, response, filename)

        except Exception as e:
                print(f"Error; {e}")
