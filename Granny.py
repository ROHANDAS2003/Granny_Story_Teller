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
global num


def s1():
    global query
    speak("do you know crow")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of crow")
        os.startfile("granny 1.0.mp3")
        time.sleep(114)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 1.0.mp3")
        time.sleep(114)
        new_story()


def s2():
    global query
    speak("do you know ant")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of ant")
        os.startfile("granny 2.0.mp3")
        time.sleep(129)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 2.0.mp3")
        time.sleep(129)
        new_story()


def s3():
    global query
    speak("do you know witch")
    speak("the witches are very dangerous")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of witch")
        os.startfile("granny 3.0.mp3")
        time.sleep(67)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 3.0.mp3")
        time.sleep(67)
        new_story()


def s4():
    global query
    speak("do you know a friend in need is a friend in deed")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story related to it")
        os.startfile("granny 4.0.mp3")
        time.sleep(56)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 4.0.mp3")
        time.sleep(56)
        new_story()


def s5():
    global query
    speak("do you know birbal")
    speak("the intelligent commander of king akbar")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of his intelligence")
        os.startfile("granny 5.0.mp3")
        time.sleep(72)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 5.0.mp3")
        time.sleep(72)
        new_story()


def s6():
    global query
    speak("do you know birbal")
    speak("the intelligent commander of king akbar")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of his intelligence")
        os.startfile("granny 6.0.mp3")
        time.sleep(44)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 6.0.mp3")
        time.sleep(44)
        new_story()


def s7():
    global query
    speak("do you have a best friend")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story named best friend")
        os.startfile("granny 7.0.mp3")
        time.sleep(79)
        new_story()
    else:
        speak("don't worry you will get one")
        speak("here's a story named best friend")
        os.startfile("granny 7.0.mp3")
        time.sleep(79)
        new_story()


def s8():
    global query
    speak("do you know dinosaurs")
    speak("actually they were in the world long time ago")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of dinosaurs")
        os.startfile("granny 8.0.mp3")
        time.sleep(120)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 8.0.mp3")
        time.sleep(120)
        new_story()


def s9():
    global query
    speak("do you know who are prince and princess")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of prince and princess")
        os.startfile("granny 9.0.mp3")
        time.sleep(66)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 9.0.mp3")
        time.sleep(66)
        new_story()


def s10():
    global query
    speak("do you know squirrels")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of squirrels")
        os.startfile("granny 10.0.mp3")
        time.sleep(83)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 10.0.mp3")
        time.sleep(83)
        new_story()


def s11():
    global query
    speak("do you like muli ke parathe")
    query = take_command().lower()
    if "yes" in query:
        speak("i like it too")
        speak("so here is a story of muli ke parathe")
        os.startfile("granny 11.0.mp3")
        time.sleep(173)
        new_story()
    else:
        speak("okay but i think you will like this story about muli ke parathe")
        os.startfile("granny 11.0.mp3")
        time.sleep(173)
        new_story()


def s12():
    global query
    speak("do you know the exams")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of exams")
        os.startfile("granny 12.0.mp3")
        time.sleep(54)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 12.0.mp3")
        time.sleep(54)
        new_story()


def s13():
    os.startfile("granny 13.0.mp3")
    time.sleep(76)
    new_story()


def s14():
    global query
    speak("do you like cookies")
    query = take_command().lower()
    if "yes" in query:
        speak("i like them too")
        speak("so here is a story of cookie monster")
        os.startfile("granny 14.0.mp3")
        time.sleep(101)
        new_story()
    else:
        speak("but you will like this cookie monster's story")
        os.startfile("granny 14.0.mp3")
        time.sleep(101)
        new_story()


def s15():
    os.startfile("granny 15.0.mp3")
    time.sleep(71)
    new_story()


def s16():
    global query
    speak("do you know birbal")
    speak("the intelligent commander of king akbar")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of his intelligence")
        os.startfile("granny 16.0.mp3")
        time.sleep(67)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 16.0.mp3")
        time.sleep(67)
        new_story()


def s17():
    global query
    speak("do you know rabbits")
    speak("they are also know as bunny")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of brave bunny")
        os.startfile("granny 17.0.mp3")
        time.sleep(79)
        new_story()
    else:
        speak("don't worry by this story, brave bunny, you get to know")
        os.startfile("granny 17.0.mp3")
        time.sleep(79)
        new_story()


def s18():
    global query
    speak("do you know tanali raman")
    speak("the intelligent commander of king krishnadevaraya")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of his intelligence")
        os.startfile("granny 18.0.mp3")
        time.sleep(83)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 18.0.mp3")
        time.sleep(83)
        new_story()


def s19():
    global query
    speak("do you know magic")
    query = take_command().lower()
    if "yes" in query:
        speak("ya so here is a story of magical kingdom")
        os.startfile("granny 19.0.mp3")
        time.sleep(173)
        new_story()
    else:
        speak("don't worry by this story you get to know")
        os.startfile("granny 19.0.mp3")
        time.sleep(173)
        new_story()




def n():
    global num
    num = random.randint(1, 20)
    n1(num)


def n1(num):
    if num == 1:
        s1()
    elif num == 2:
        s2()
    elif num == 3:
        s3()
    elif num == 4:
        s4()
    elif num == 5:
        s5()
    elif num == 6:
        s6()
    elif num == 7:
        s7()
    elif num == 8:
        s8()
    elif num == 9:
        s9()
    elif num == 10:
        s10()
    elif num == 11:
        s11()
    elif num == 12:
        s12()
    elif num == 13:
        s13()
    elif num == 14:
        s14()
    elif num == 15:
        s15()
    elif num == 16:
        s16()
    elif num == 17:
        s17()
    elif num == 18:
        s18()
    elif num == 19:
        s19()
    elif num == 20:
        s20()


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
        story()
    elif "do not know" in query:
        speak("okay, so you seems like confused about so many choices. its totally normal")
        speak("when someone have many choices they are confused")
        speak("but guess what, that's where your granny could help you")
        speak("I know which story you should listen right now")
        story()
    elif "your choice" in query:
        speak("okay, of my choice haa")
        speak("actually i remember one, would you like to listen it")
        query = take_command().lower()
        if "yes" in query:
            speak("so, i am starting the story. be quite and listen carefully")
            story()
        elif "sure" in query:
            speak("so, i am starting the story. be quite and listen carefully")
            story()
        else:
            speak("seems you are in mood to tease your granny. don't do so, let me tell the story")
            speak("so now, i am starting the story. be quite and listen carefully")
            story()
    elif "any" in query:
        speak("okay, of my choice haa")
        speak("actually i remember one, would you like to listen it")
        query = take_command().lower()
        if "yes" in query:
            speak("so, i am starting the story. be quite and listen carefully")
            story()
        elif "sure" in query:
            speak("so, i am starting the story. be quite and listen carefully")
            story()
        else:
            speak("seems you are in mood to tease your granny. don't do so, let me tell the story")
            speak("so now, i am starting the story. be quite and listen carefully")
            story()
    elif "anyone" in query:
        speak("okay, of my choice haa")
        speak("actually i remember one, would you like to listen it")
        query = take_command().lower()
        if "yes" in query:
            speak("so, i am starting the story. be quite and listen carefully")
            story()
        elif "sure" in query:
            speak("so, i am starting the story. be quite and listen carefully")
            story()
        else:
            speak("seems you are in mood to tease your granny. don't do so, let me tell the story")
            speak("so now, i am starting the story. be quite and listen carefully")
            story()
    elif "like to tell" in query:
        speak("okay, of my choice haa")
        speak("actually i remember one, would you like to listen it")
        query = take_command().lower()
        if "yes" in query:
            speak("so, i am starting the story. be quite and listen carefully")
            story()
        elif "sure" in query:
            speak("so, i am starting the story. be quite and listen carefully")
            story()
        else:
            speak("seems you are in mood to tease your granny. don't do so, let me tell the story")
            speak("so now, i am starting the story. be quite and listen carefully")
            story()
    elif "don't want" in query:
        speak("so, should i go to sleep")
        query = take_command().lower()
        if "yes" in query:
            sleep()
        elif "sure" in query:
            sleep()
        else:
            speak("so, it seems as you are teasing you are granny")
            speak("don't do that")
            speak("now, i am starting a story")
            story()
    elif "do not want" in query:
        speak("so, should i go to sleep")
        query = take_command().lower()
        if "yes" in query:
            sleep()
        elif "sure" in query:
            sleep()
        else:
            speak("so, it seems as you are teasing you are granny")
            speak("don't do that")
            speak("now, i am starting a story")
            story()
    else:
        wished()


def not_wished():
    global query
    speak("you should wish when someone wishes you, okay")
    speak("so, what do you like the most")
    query = take_command().lower()
    if "nothing" in query:
        speak("okay, but i am sure that, now onwards you will like this story the most")
        speak("so now, i am starting the story. be quite and listen carefully")
        story()
    else:
        speak("yaa, i like it too")
        speak("but you know that i like this story the most")
        story()


def story():
    n()


def new_story():
    global query
    speak("Want to listen one more")
    query = take_command().lower()
    if "yes" in query:
        story()
    elif "sure" in query:
        story()
    elif "no" in query:
        speak("so, should i go to sleep")
        query = take_command().lower()
        if "yes" in query:
            sleep()
        elif "sure" in query:
            sleep()
        else:
            speak("so, it seems as you are teasing you are granny")
            speak("don't do that")
            speak("now, i am starting a story")
            story()
    else:
        story()


def sleep():
    speak("sleeping...")
    speak("you should go and do your home work")
    speak("bye..")
    exit()


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
    if wish in query:
        wished()
    else:
        not_wished()
