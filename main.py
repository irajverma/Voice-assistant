import pyttsx3 as p
import  speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import webbrowser
import openai




engine = p.init()# initalize
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voice = engine.getProperty('voices')
# engine.setProperty('voice',voice[0].id)# for male voice
engine.setProperty('voice',voice[1].id)
# print(voice)
# print(rate)
openai.api_key= "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"


def speak(texts): 
    print(f" {texts}")
    engine.say(texts)
    engine.runAndWait()
r =  sr.Recognizer()#retrieve data from the microphone
speak("Hello boss. My name is carrot")

# def openai_1(query):
#    chat =[]
#    chat.append({"role":"user", "context": query})
#    response = openai.ChatCompletion.create(
#        model = "gpt-3.5-turbo",
#        message = chat
#    )


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
    return texts


# text = command()
# if "what" and "about" and "you" in text:
#     speak("I am having a great time sir")
# speak("how can i help you")

def hello():
    speak("Hello sir. how are you?")

def i_am_fine():
    speak("That's great sir")

def how_are_you():
    speak("I am perfect sir")

def thank_you():
    speak("You're welcome, sir")

def controls(query):
    if "pause" in query:
        pyautogui.press("k")
        speak("video paused")
    elif"play" in query:
        pyautogui.press("k")
        speak("video played")
    elif"mute" in query:
        pyautogui.press("m")
        speak("video mute")
    elif "volume up" in query:
        from keyboard import volumeup
        speak("turning volume up, sir")
        volumeup()
    elif "volume down" in query:
        from keyboard import volumedown
        speak("turning volume up, sir")
        volumedown()

def tired():
    speak("This might cheer you up , Sir")
    webbrowser.open("https://www.youtube.com/watch?v=H60L40GbfFI")



def opening(query):
    from openapp import openappweb
    openappweb(query)

def closing(query):
    from openapp import closeappweb
    closeappweb(query)

def google(query):
    from _googlesearch import searchgoogle
    searchgoogle(query)

def youtube(query):
    from _googlesearch import searchyoutube
    searchyoutube(query)

def wikipedia(query):
    from _googlesearch import searchwiki
    searchwiki(query)

def news():
    from newsread import latestnews
    latestnews()


def game():
    speak("To play TIC TAC TOE press 1 and to play ROCK PAPER SCISSORS press 2")
    choice=command().lower()
    print(choice)
    if choice == "tic tac toe":
        from games import random
        random()
    elif choice == "rock paper Scissors":
        from games import rps
        rps()

def calculate(query):
    from calculator import wolf
    from calculator import Calc
    query = query.replace("calculate","")
    query = query.replace("friday","")
    Calc(query )

def whatsapp():
    from whatsapp import sendMessage
    sendMessage()

def shutdown_system(query):
    speak("Are You sure you want to shutdown? yes or no!")
    shutdown = input(command())
    if shutdown == "yes":
        os.system("shutdown /s /t 1")
    elif shutdown == "no":
        pass

def schedule(query):
    tasks = [] #Empty list 
    speak("Do you want to clear old tasks (speak YES or NO)")
    query = command().lower()
    if "yes" in query:
        file = open("tasks.txt","w")
        file.write(f"")
        file.close()
        no_tasks = int(input("Enter the no. of tasks :- "))
        i = 0
        for i in range(no_tasks):
            tasks.append(input("Enter the task :- ",command()))
            print(tasks)
            speak(f"Is this your task {tasks} . say yes and no")
            check = command().lower()
            if "yes " in check:
                file = open("tasks.txt","a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()
            elif "no" in check:
                i -=1



                
    elif "no" in query:
        i = 0
        for i in range(no_tasks):
            tasks.append(input("Enter the task :- ",command()))
            print(tasks)
            speak(f"Is this your task {tasks} . say yes and no")
            check = command().lower()
            if "yes " in check:
                file = open("tasks.txt","a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()
            elif "no" in check:
                i -=1



def temp(query):
    search = "temperature in kanpur"
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current{search} is {temp}")

def weather(query):
    search = "weather in kanpur"
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    waeth = data.find("div", class_ = "BNeawe").text
    speak(f"current{search} is {waeth}")

def time(query):
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"Sir, the time is {strTime}")

def alarm(a):
    timehere = open("alarmtext.txt","a")
    timehere.write(a)
    timehere.close()
    os.startfile("alarm.py")

def alarmtime():
    print("input time example:- 10 and 10 and 10")
    speak("Set the time")
    a = input("Please tell the time :- ")
    alarm(a)
    speak("Done,sir")


def shut_down(query):
    speak("going to shutdown")
    exit()



if __name__ == "__main__":
    dict_comm = {
    "hello": hello,
    "i am fine": i_am_fine,
    "how are you": how_are_you,
    "thank you": thank_you,
    "google":lambda: google(query),
    "youtube":lambda: youtube(query),
    "wikipedia":lambda: wikipedia(query),
    "temperature":lambda:temp(query),
    "weather":lambda:weather(query),
    "time":lambda:time(query),
    "turn off": lambda:shut_down(query),
    "open":lambda: opening(query),
    "close":lambda: closing(query),
    "set an alarm":lambda:alarmtime(),
    "pause":lambda:controls(query),
    "play the vedior":lambda:controls(query),
    "volume up":lambda:controls(query),
    "volume down":lambda:controls(query),
    "tired": lambda: tired(),
    "news": lambda:news(),
    "calculate":lambda:calculate(query),
    "whatsapp": lambda:whatsapp(),
    "shutdown system":lambda:shutdown_system(),
    "play game":lambda:game()
    }
    while True:
        query = command().lower()
        if "wake up" in query:
            from _greetme import greetme
            greetme()
            

            while True:
                query = command().lower()
                for key, value in dict_comm.items():
                    if key in query:
                        value()
                        break
                else:
                    if "go to sleep" in query:
                        speak("Okay sir, You can call me anytime")
                        break
                    # else:
                    #     openai_1(query)