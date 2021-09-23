# this is the "game.py" file...

import random
import os
from dotenv import load_dotenv
load_dotenv()
PLAYER_NAME = os.getenv("PLAYER_NAME")

print("Welcome", PLAYER_NAME, "to my rock, paper, scissors game!")
print("Rock, Paper, Scissors, Shoot!")

# PROMPT USER FOR INPUT

user_choice = input("Choose 'rock' or 'paper' or 'scissors':")
print("----------")
print(PLAYER_NAME, "chose:")
print (user_choice)

# VALIDATING USER INPUT

if user_choice in ["rock", "paper", "scissors"]:
    print("And...")
else:
    print ("Sorry, that is not a valid option. Try playing again with a different choice!")
    quit ()

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)
print("----------")

# DETERMINING A WINNER

if user_choice == "rock":
    if computer_choice == "scissors":
        print("Congratulations", PLAYER_NAME, "you won!")
    elif computer_choice == "paper":
        print("Computer won, better luck next time!")
    elif computer_choice == "rock":
        print("tie, play again!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Congratulations", PLAYER_NAME, "you won!")
    elif computer_choice == "rock":
        print ("Computer won, better luck next time!")
    elif computer_choice == "scissors":
        print ("tie, play again")
elif user_choice == "paper":
    if computer_choice == "rock":
        print ("Congratulations", PLAYER_NAME, "you won!")
    elif computer_choice == "scissors":
        print ("Computer won, better luck next time!")
    elif computer_choice == "paper":
        print ("tie, play again!")

print("Thanks for playing", PLAYER_NAME,"!")


