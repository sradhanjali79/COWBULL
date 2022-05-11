import random

def cowbull():
    list1=[0,1,2,3,4,5,6,7,8,9]
    list2=[]
    x=random.sample(list1,5)
    bull=[]
    cow=[]
    for i in range(10):
        x=int(input("enter any num..."))
        y=int(input("enter position..."))
        if x in list2:
            p=list2.index(x)
            if y==p:
                bull.insert(y,x)
                print("bull",bull)
            else:
                cow.append(x)
                print("cow ",cow)
        else:
            print("sorry this no. is not exist")
    if bull==list2:
        print("congratulation",user,"you are the winner")
    else:
        print("opps",user,"you are the looser")
    again=input("Do u want to play again...")
    if again=="yes":
        cowbull()
    else:
        print("Bye")
    
user=input("enter your name...")
print("  welcome",user,"  ")
print("[0,1,2,3,4,5,6,7,8,9]")
cowbull()

