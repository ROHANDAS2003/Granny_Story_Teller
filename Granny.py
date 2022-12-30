import speech_recognition as sr
import pyttsx3
import datetime
import random
import os
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    global wish
    if 12 > hour >= 4:
        wish = "good morning"
        print("good morning")
        speak(wish)
    elif 17 > hour >= 12:
        wish = "good afternoon"
        print("good afternoon")
        speak(wish)
    elif 21 > hour >= 17:
        wish = "good evening"
        print("good evening")
        speak(wish)
    elif 4 > hour >= 21:
        wish = "good night"
        print("good night")
        speak(wish)


if __name__ == "__main__":
    wish_me()
    speak("I am your Virtual granny, You can call me granny")
