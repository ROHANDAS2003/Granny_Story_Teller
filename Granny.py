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

global query
global wish
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


def wished():
    global query
    speak("which story do you want to listen")
    query = take_command().lower()
    if "don't know" in query:
        speak("okay, so you seems like confused about so many choices. its totally normal")
        speak("when someone have many choices they are confused")
        speak("but guess what, that's where your granny could help you")
        speak("I know which story you should listen right now")
    elif "do not know" in query:
        speak("okay, so you seems like confused about so many choices. its totally normal")
        speak("when someone have many choices they are confused")
        speak("but guess what, that's where your granny could help you")
        speak("I know which story you should listen right now")
    elif "your choice" in query:
        speak("okay, of my choice haa")
        speak("actually i remember one, would you like to listen it")
        query = take_command().lower()
        if "yes" in query:
            speak("so, i am starting the story. be quite and listen carefully")
        elif "sure" in query:
            speak("so, i am starting the story. be quite and listen carefully")
        else:
            speak("seems you are in mood to tease your granny. don't do so, let me tell the story")
            speak("so now, i am starting the story. be quite and listen carefully")
    elif "any" in query:
        speak("okay, of my choice haa")
        speak("actually i remember one, would you like to listen it")
        query = take_command().lower()
        if "yes" in query:
            speak("so, i am starting the story. be quite and listen carefully")
        elif "sure" in query:
            speak("so, i am starting the story. be quite and listen carefully")
        else:
            speak("seems you are in mood to tease your granny. don't do so, let me tell the story")
            speak("so now, i am starting the story. be quite and listen carefully")
    elif "anyone" in query:
        speak("okay, of my choice haa")
        speak("actually i remember one, would you like to listen it")
        query = take_command().lower()
        if "yes" in query:
            speak("so, i am starting the story. be quite and listen carefully")
        elif "sure" in query:
            speak("so, i am starting the story. be quite and listen carefully")
        else:
            speak("seems you are in mood to tease your granny. don't do so, let me tell the story")
            speak("so now, i am starting the story. be quite and listen carefully")
    elif "like to tell" in query:
        speak("okay, of my choice haa")
        speak("actually i remember one, would you like to listen it")
        query = take_command().lower()
        if "yes" in query:
            speak("so, i am starting the story. be quite and listen carefully")
        elif "sure" in query:
            speak("so, i am starting the story. be quite and listen carefully")
        else:
            speak("seems you are in mood to tease your granny. don't do so, let me tell the story")
            speak("so now, i am starting the story. be quite and listen carefully")
    elif "don't want" in query:
        speak("so, should i go to sleep")
        query = take_command().lower()
        if "yes" in query:
        elif "sure" in query:
        else:
            speak("so, it seems as you are teasing you are granny")
            speak("don't do that")
            speak("now, i am starting a story")
    elif "do not want" in query:
        speak("so, should i go to sleep")
        query = take_command().lower()
        if "yes" in query:
        elif "sure" in query:
        else:
            speak("so, it seems as you are teasing you are granny")
            speak("don't do that")
            speak("now, i am starting a story")
    else:
        wished()
def take_command():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
    try:
        print("Recognising")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print(e)
        return "None"
    return query


if __name__ == "__main__":
    wish_me()
    speak("I am your Virtual granny, You can call me granny")
    query = take_command().lower()
        wished()
