from random import randint

#create a list of play options
t = ["rock", "paper", "scissors"]

#this assigns a value to the computer: the randomly generated number corresponds to the list above
computer = t[randint(0,2)]

n = True
#this is to create a loop which keeps the game running after each turn
while n == True:
    player = input("Rock [r], Paper [p], Scissors [s]: ")
    if player == computer:
        print("It's a tie!")
    elif player == "r":
        if computer == "paper":
            print("You lose!", computer, "beats rock")
        else:
            print("You win! Rock beats", computer)
    elif player == "p":
        if computer == "Scissors":
            print("You lose!", computer, "beats paper")
        else:
            print("You win! Paper beats", computer)
    elif player == "s":
        if computer == "Rock":
            print("You lose...", computer, "beats scissors")
        else:
            print("You win! Scissors beats", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    n = True
    computer = t[randint(0,2)]
