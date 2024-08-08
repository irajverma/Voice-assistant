import pyttsx3 as p
import datetime
import os

engine = p.init()# initalize
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voice = engine.getProperty('voices')
# engine.setProperty('voice',voice[0].id)# for male voice
engine.setProperty('voice',voice[1].id)
# print(voice)
# print(rate)



def speak(texts): 
    print(f" {texts}")
    engine.say(texts)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("friday","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("harvard.wav") #You can choose any music or ringtone 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)