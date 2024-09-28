import random
def game():
    computer=random.choice([-1,0,1])
    user=input("Your turn : ")
    dic={-1:"stone",0:"paper",1:"scissor"}
    reverse_dic={"stone":-1,"paper":0,"scissor":1}
    you=reverse_dic[user]
    print(f"\nYour choice is {user}")
    print(f"Computer choice is {dic[computer]}")
    if(computer ==  you):
        print("The game is draw.. !")
    else:
        if(computer==-1 and you==0):                
            print("You won.. !")
        elif(computer==0 and you==-1):              
            print("You lose.. !")     
        elif(computer==0 and you==1):               
            print("You won.. !")
        elif(computer==1 and you==0):               
            print("You lose.. !")
        elif(computer==1 and you==-1):              
            print("You won.. !")
        elif(computer==-1 and you==1):              
            print("You lose.. !")
        else:
            print("Something went wrong... ! ")
game()