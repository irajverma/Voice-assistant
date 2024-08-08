import pyttsx3 as p
import  datetime


engine = p.init()# initalize
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)


def speak(text): 
    print(text)
    engine.say(text)
    engine.runAndWait()


def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("good morning,sir")
    elif hour>12 and hour<=18:
        speak("goof afternoon,sir")
    else:
        speak("good evening,sir")
    speak("please tell me, How can I help you?")