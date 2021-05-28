# game.py
#Import Modules
import random
import os
import dotenv

#Get player name from .env file
dotenv.load_dotenv()
PLAYER_NAME = os.getenv("PLAYER_NAME")

#Initial Game Heading
print("---------")
print(f"Welcome {PLAYER_NAME} to Rock, Paper, Scissors")
print("---------")


#Prompt user to choose and display choice
user_choice = input("Please choose on of 'rock', 'paper', 'scissor' ")
#Validate User Choice
#Opted for while loop to allow user to enter multiple values rather than exit program
while user_choice not in ("rock", "paper", "scissor"):
    print("You selection is invalid")
    user_choice = input("Please choose rock paper or scissor ")
print(f"You have selected {user_choice}")


#Create Array for possible choices
arr = ["rock", "paper", "scissor"]
comp = random.choice(arr)
#Output Computer's choice
print("The computer chose ", comp)

#Logic for choosing winner
if user_choice == comp:
    print("The game ends in a draw")
elif (user_choice == "rock" and comp == "scissor") or (user_choice == "scissor" and comp == "paper") or (user_choice == "paper" and comp == "rock"):
    print("Player has won the game")
else:
    print("The Computer has won")


print("This is the nend of our game.  Please play again")