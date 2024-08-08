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
            print(f"{bndr1} wins")
            return 1
        if(sum(y[w[0]-1],y[w[1]-1],y[w[2]-1])==3):
            print(f"{bndr2} wins")
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
print("Welcome to tic tac toe")
bndr1 = input("enter the name for X")
bndr2 = input("enter the name for O")
while(True):
    z += 1
    board(x,y)
    if(a==1):
        print(f"{bndr1}'s chance")
        value = int(input("Enter the number"))
        if(value>9 or value<1  ):
            print("enter number between 1 to 9")
            z -=1
            continue
        if( repetition(value,c)):
            print("Don't repeat the same number")
            z -=1
            continue
        # elif(  repetition(value,x) or repetition(value,y)):
        #     print("Don't repeat the same number")
        #     continue
        c[value] ='*'
        x[value-1] = 1
    else:
        print(f"{bndr2}'s chance")
        value = int(input("Enter the number"))
        if(value>9 or value<1 ):
            print("enter number between 1 to 9 ")
            z -=1
            continue 
        if( repetition(value,c)):
            print("Don't repeat the same number")
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
        print("lol noone wins....try again")
        break
#game over............................DONE
# number between 1 to 9...............DONE
# no repetition of number.............DONE
#z have issues........................DONE
# only use int 