import wolframalpha
import pyttsx3 as p
import speech_recognition

engine = p.init()# initalize
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)


def speak(texts): 
    print(f" {texts}")
    engine.say(texts)
    engine.runAndWait()



def wolf(query):
    apikey=("WKVKA2-KL2GT3YTJ6")
    requester = wolframalpha.Client(query)
    requested = requester.query(query)


    try :
        answer = next(requested.results).text
        return answer
    except:
        speak("the value is not answerable")


def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("into","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("by","/")

    final = str(Term)
    try:
        Result = wolframalpha(final)
        print(f"{Result}")
        speak(Result)
    except:
        speak("the value is not answerable")