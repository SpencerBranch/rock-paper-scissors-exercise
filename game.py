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

#Creating a loop to play
play_again = "yes"
while play_again == "yes":

    #Prompt user to choose and display choice
    user_choice = input("Please choose on of 'rock', 'paper', 'scissor' ")
    #Validate User Choice
    #Opted for while loop to allow user to enter multiple values rather than exit program
    while user_choice not in ("rock", "paper", "scissor"):
        print("You selection is invalid")
        user_choice = input("Please choose 'rock', 'paper', or 'scissor' ")
    print(f"You have selected {user_choice}")


    #Create Array for possible choices
    arr = ["rock", "paper", "scissor"]
    comp = random.choice(arr)
    #Output Computer's choice
    print("The computer chose ", comp)

    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissor": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissor": "scissor"
        },
        "scissor": {
            "rock": "rock",
            "paper": "scissor",
            "scissor": None,
        }
    }

    winner = winners[user_choice][comp]
    if winner == user_choice:
        print("YOU WON!")
    elif winner == comp:
        print("YOU LOST")
    else:
        print("TIE")

   #     #Logic for choosing winner
    #    if user_choice == comp:
    #        print("The game ends in a draw")
    #   elif (user_choice == "rock" and comp == "scissor") or (user_choice == "scissor" and comp == "paper") or (user_choice == "paper" and comp == "rock"):
    #      print("Player has won the game")
    #    else:
    #        print("The Computer has won")
    play_again = input("would you like to play again? (yes/no) ")


print("Thanks for playing, please play again soon!")