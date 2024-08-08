import pywhatkit
import pyttsx3 as p
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime


engine = p.init()# initalize
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)


def speak(texts): 
    print(f" {texts}")
    engine.say(texts)
    engine.runAndWait()
r =  sr.Recognizer()



def command():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        # r.adjust_for_ambient_noise(source , 1.2)
        print("listening")
        audio = r.listen(source,0)
    try:
        print("understanding ....")
        texts = r.recognize_google(audio)#use the google api to convert the speech to text
        print(texts) 
    except:
        print("say that again")
        return "none"
    # return texts



strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you wan to message")
    a = int(input(speak("For chotu bacha press 1 . For Bhaiya press 2")))
    if a == 1:
        speak("Whats the message")
        message = str(input(command()))
        pywhatkit.sendwhatmsg("+916393266292",message,time_hour=strTime,time_min=update)
    elif a==2:
        speak("Whats the message")
        message = str(input(command()))
        pywhatkit.sendwhatmsg("+917355423934",message,time_hour=strTime,time_min=update)