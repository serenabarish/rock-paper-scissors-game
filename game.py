# this is the "game.py" file...

import random

print("Welcome 'Player One' to my Rock, Paper, Scissors Game!")
print("Rock, Paper, Scissors, Shoot!")

# PROMPT USER FOR INPUT

user_choice = input("Choose 'rock' or 'paper' or 'scissors':")
print("User chose:")
print (user_choice)

# VALIDATING USER INPUT
if user_choice in ["rock", "paper", "scissors"]:
    print("And...")
else:
    print ("Sorry, try again playing with a different choice!")
    quit ()

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)

# DETERMINING A WINNER

if user_choice == "rock":
    if computer_choice == "scissors":
        print("Congratulations 'Player One', you won!")
    if computer_choice == "paper":
        print("Computer won, better luck next time!")
    if computer_choice == "rock":
        print("tie, play again!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Congratulations 'Player One', you won!")
    if computer_choice == "rock":
        print ("Computer won, better luck next time!")
    if computer_choice == "scissors":
        print ("tie, play again")
elif user_choice == "paper":
    if computer_choice == "rock":
        print ("Congratulations 'Player One', you won!")
    if computer_choice == "scissors":
        print ("Computer won, better luck next time!")
    if computer_choice == "paper":
        print ("tie, play again!")

print("Thanks for playing!")


