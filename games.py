import random
import re
import pyttsx3 as p
import speech_recognition as sr


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



def random():
    def sum(a,b,c):
        return a+b+c
    def board(x,y):
        one = 'X' if x[0] else('O' if y[0] else 1)
        two = 'X' if x[1] else('O' if y[1] else 2)
        three = 'X' if x[2] else('O' if y[2] else 3)
        four= 'X' if x[3] else ('O'if y[3] else 4)
        five= 'X' if x[4] else ('O'if y[4] else 5)
        six= 'X' if x[5] else ('O'if y[5] else 6)
        seven = 'X' if x[6] else('O' if y[6] else 7)
        eight = 'X' if x[7] else('O' if y[7] else 8)
        nine = 'X' if x[8] else('O' if y[8] else 9)
        print(f"{one}|{two}|{three}")
        print ("-|-|-")
        print(f"{four}|{five}|{six}")
        print ("-|-|-")
        print(f"{seven}|{eight}|{nine}")


    #123
    #456
    #789
    def check(x,y):
        wins = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[7,5,3],[1,4,7],[2,5,8],[3,6,9]]
        for w in wins:
            if (sum(x[w[0]-1],x[w[1]-1],x[w[2]-1])==3):
                speak(f"{bndr1} wins")
                return 1
            if(sum(y[w[0]-1],y[w[1]-1],y[w[2]-1])==3):
                speak(f"{bndr2} wins")
                return 0
        return -1

    def repetition(value, a):

        # for n in a[value]:
            if(a[value]=='*'):
                return True
            else:
                 return False
        # if (m[value - 1] == value):
        #     return True
        # else:
        #     return False
        # m[value - 1] = value



    x = [0,0,0,0,0,0,0,0,0]
    y = [0,0,0,0,0,0,0,0,0]
    c = ['*',1,2,3,4,5,6,7,8,9]
        #1,2,3,4,5,6,7,8,9,]
    # d = [0,0,0,0,0,0,0,0,0,0]
    #     #0,1,2,3,4,5,6,7,8,9,]

    a = 1
    z=1
    speak("Welcome to tic tac toe")
    speak("enter the name for X")
    bndr1 = input()
    speak("enter the name for O")
    bndr2 = input()
    while(True):
        z += 1
        board(x,y)
        if(a==1):
            speak(f"{bndr1}'s chance")
            speak("Enter the number")
            value = int(input())
            if(value>9 or value<1  ):
                speak("enter number between 1 to 9")
                z -=1
                continue
            if( repetition(value,c)):
                speak("Don't repeat the same number")
                z -=1
                continue
            # elif(  repetition(value,x) or repetition(value,y)):
            #     print("Don't repeat the same number")
            #     continue
            c[value] ='*'
            x[value-1] = 1
        else:
            speak(f"{bndr2}'s chance")
            speak("Enter the number")
            value = int(input())
            if(value>9 or value<1 ):
                speak("enter number between 1 to 9 ")
                z -=1
                continue 
            if( repetition(value,c)):
                speak("Don't repeat the same number")
                z -=1
                continue
            # elif(repetition(value,x) or repetition(value,y)):
            #     print("Don't repeat the same number")
            #     continue
            c[value] ='*'
            y[value-1] = 1
        cwin = check(x,y)
        if(cwin != -1):
            break
        a = 1-a
        if (z==10):
            speak("lol noone wins....try again")
            break
    #game over............................DONE
    # number between 1 to 9...............DONE
    # no repetition of number.............DONE
    #z have issues........................DONE
    # only use int 




## ROCK PAPER SCISSORS
def rps():
    while(0<=2):
        speak("Rock Paper Scissors!!!")
        speak("Enter your name : ")
        name = input()
        speak("Enter R for Rock , P for Paper , S for Scissors and E to exit the match  :  ")
        choice = input()

        if(not re.match("[SsRrPpEe]",choice) or len(choice) != 1):
            speak("choose a letter:")
            speak("R , P , S , E")
            continue

        if(choice == "e" or choice =="E"):
            speak("Exit the loop")
            break
        compopt = ['R','P','S']
        compchoice = random.choice(compopt)
        speak(f"COMPUTER'S choose  :  {compchoice}")
        speak(f"{name.upper()}'s choose  :  {choice.upper()}")

        
        if( compchoice == choice.upper()):
            speak("Game Tie")
        elif(compchoice == 'R' and choice.upper() == 'S'):
            speak("Computer wins")
            continue

        elif(compchoice == 'P' and choice.upper() == 'R'):
            speak("Computer wins")
            continue

        elif(compchoice == 'S' and choice.upper() == 'P'):
            speak("Computer wins")
            continue
        else:
            speak("You win!")
            # continue


rps()