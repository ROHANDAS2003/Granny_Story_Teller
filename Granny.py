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


if __name__ == "__main__":
