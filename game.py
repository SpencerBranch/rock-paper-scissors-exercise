# game.py
#Import Modules
import random


#Initial Game Heading
print("Rock, Paper, Scissors, Shoot!")


user_choice = input("Please choose on of 'rock', 'paper', 'scissor' ")

print("User Choice: ", user_choice)

#Validate User Choice
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissor"):
    print("Valid Choice")
else:
        print("Not a valid choice")
        exit()


#Create Array for possible choices
arr = ["rock", "paper", "scissor"]

comp = random.choice(arr)

print("The computer chose ", comp)

if user_choice == comp:
#if (user_choice == "rock" and comp == "rock") or (user_choice == "paper" and comp == "paper") or (user_choice == "scissor" and comp== "scissor"):
    print("The game ends in a draw")
elif (user_choice == "rock" and comp == "scissor") or (user_choice == "scissor" and comp == "paper") or (user_choice == "paper" and comp == "rock"):
    print("Player has won the game")
else:
    print("The Computer has won")




print("This is the nend of our game.  Please play again")