import random
import re

while(0<=2):
    print("Rock Paper Scissors!!!")
    name = input("Enter your name : ")
    
    choice = input("Enter R for Rock , P for Paper , S for Scissors and E to exit the match  :  ")

    if(not re.match("[SsRrPpEe]",choice) or len(choice) != 1):
        print("choose a letter:")
        print("R , P , S , E")
        continue

    if(choice == "e" or choice =="E"):
        print("Exit the loop")
        break
    compopt = ['R','P','S']
    compchoice = random.choice(compopt)
    print(f"COMPUTER'S choose  :  {compchoice}")
    print(f"{name.upper()}'s choose  :  {choice.upper()}")

    
    if( compchoice == choice.upper()):
        print("Game Tie")
    elif(compchoice == 'R' and choice.upper() == 'S'):
        print("Computer wins")
        continue

    elif(compchoice == 'P' and choice.upper() == 'R'):
        print("Computer wins")
        continue

    elif(compchoice == 'S' and choice.upper() == 'P'):
        print("Computer wins")
        continue
    else:
        print("You win!")
        # continue