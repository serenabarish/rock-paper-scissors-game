# Rock Paper Scissors Game - Python

A classic rock, paper, scissors game against a computer.

## Prerequisites
* Anaconda 3.7
* Python 3.7
* Pip

## Installation
Fork this [remote repository] (https://github.com/serenabarish/rock-paper-scissors-game) under your own control, then download your remote copy onto your local computer. Then navigate from the command line to the root directory before running the other commands.
````
cd desktop/rock-paper-scissors-game
````

Create and activate and new Anaconda virtual environment.
````
conda create -n game-env python=3.7 # first time only
conda activate game-env
````
After activating the virtual environment, install package dependencies (see the [requirements.txt](/requirements.txt) file):
````sh
pip install -r requirements.txt
````

## Setup
In the root directory of your local repository, create a new file called ".env" and create a new variable called "Player_Name" stored in the ".env" file.

## Usage
Run the Python script:
````
python game.py
````