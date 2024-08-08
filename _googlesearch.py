import speech_recognition as sr
import pyttsx3 as p
import pywhatkit as pw
import wikipedia
import webbrowser as wb


r = sr.Recognizer()

def command():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source , 1.2)
        print("listening")
        audio = r.listen(source,0)

    try:
        print("understanding ....")
        text = r.recognize_google(audio)#use the google api to convert the speech to text
        print(text) 
    except:
        print("say that again")
        return "none"
    return text

query = command().lower()

engine = p.init()# initalize
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak(text): 
    print(text)
    engine.say(text)
    engine.runAndWait()
r =  sr.Recognizer()#retrieve data from the microphone

def searchgoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("friday","")
        query = query.replace("on google","")
        query = query.replace("from google","")
        query = query.replace("google","")
        query = query.replace("search","")
        speak("this is what i found on google")

        try:
            pw.search(query)
            result = googleScrap.summary(query,3)
            speak(result)
            speak("done sir")
        except:
            speak("no speakable output avialable")

def searchyoutube(query):
    if "youtube" in query:

        speak("This is what i found for your search!")
        query = query.replace(" on youtube","")
        query = query.replace("youtube","")
        query = query.replace("friday","")
        query = query.replace("search ","")
        query = query.replace("play ","")
        web = "https://www.youtube.com/results?search_query="+query
        wb.open(web)
        pw.playonyt(query)
        speak("done sir")
        

def searchwiki(query):
    if "wikipedia" in query:
        speak("search from wikipedia!")
        query = query.replace("on wikipedia","")
        query = query.replace("from wikipedia","")
        query = query.replace("wikipedia","")
        query = query.replace("search","")
        query = query.replace("friday","")
        result = wikipedia.summary(query,3)
        speak("according to wikipedia")
        print(result)
        speak(result)
        speak("done sir")
