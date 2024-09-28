import random
def game():
    computer=random.choice([-1,0,1])

    user=input("Your turn : ")

    dic={-1:"stone",0:"paper",1:"scissor"}
    reverse_dic={"stone":-1,"paper":0,"scissor":1}

    you=reverse_dic[user]
    
    print(f"\nYour choice is {user}")
    print(f"Computer choice is {dic[computer]}")
    
    if(computer-you==0): 
        print("The game is draw.. !")
    elif(computer-you==-1 or computer-you==2 ):
        print("You Won.. ! ")
    else:
        print("You lose.. ! ")            

game() 