from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock [r], Paper [p], Scissors [s]: ")
    if player == computer:
        print("You tied!")
    elif player == "r":
        if computer == "Paper":
            print("You lose!", computer, "beats Rock")
        else:
            print("You win!", "Rock beats", computer)
    elif player == "p":
        if computer == "Scissors":
            print("You lose!", computer, "beats Paper")
        else:
            print("You win!", "Paper beats", computer)
    elif player == "s":
        if computer == "Rock":
            print("You lose...", computer, "beats Scissors")
        else:
            print("You win!", "Scissors beats", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)]
