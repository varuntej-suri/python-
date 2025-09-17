import random
option=["rock","paper","scissors"]

run=True
while run :
    player=None
    computer=random.choice(option)
    while player not in option:
        player=input("Enter the your chioce (rock ,paper,scissors): ")
   
    print(f"player={player}")
    print(f"computer={computer}")
    if player==computer:
         print("it's tie")
    elif player=="rock" and computer=="scissors" :
          print("you win")
    elif player=="scissors" and computer =="paper": 
         print("you win")
    elif player=="paper" and computer=="rock" :
         print("you win")
    else:
        print("you lose")
    print("Enter do you wnat continue:")
    h=input("Enter  y to continue").lower()
    if h=="y":
        run=True
    else:
        run=False