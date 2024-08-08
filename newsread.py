import requests
import json
import pyttsx3 as p

engine = p.init()# initalize
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)


def speak(texts): 
    print(f" {texts}")
    engine.say(texts)
    engine.runAndWait()



def latestnews():
    newsdict = {"bussiness":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=ef5d8a720a8649a9a71b05d84e424628",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=ef5d8a720a8649a9a71b05d84e424628",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=ef5d8a720a8649a9a71b05d84e424628",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=ef5d8a720a8649a9a71b05d84e424628",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=ef5d8a720a8649a9a71b05d84e424628",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ef5d8a720a8649a9a71b05d84e424628"
           }
    
    content = None
    url = None
    print("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key,value in newsdict.items():
        if key.lower() in field.lower():
            url = value
            # print(url)
            speak("url was found")
            break
        else:
            url = True
    if url == True:
        speak("url not found")

    news = requests.get(url).text
    news = json.load(news)
    speak("here is the first news")

    art = news("articles")
    for articles in art:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more imfo visit{news_url}")

        a = input(speak("[press 1 to continue] and [press 2 to stop]"))
        if int(a) == 1:
            pass
        elif int(a) == 2:
            break


    speak("thats all")