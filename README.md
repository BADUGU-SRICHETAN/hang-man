### Hangman Game
A console-based Hangman game implemented in Python. This game allows players to choose from a variety of categories and guess the word by entering letters one at a time. The game visually represents the hangman and tracks the remaining attempts, calculating a score based on the number of remaining attempts when the word is guessed correctly.

### Features
Multiple Categories: Choose from various categories such as Programming, Animals, Countries, and more.

Visual Representation: ASCII art to display the hangman and track the player's progress.

Scoring System: Score based on the remaining attempts after guessing the word.

Input Validation: Ensures valid letter or word inputs, preventing repeated guesses.

Random Word Selection: Each game features a randomly selected word from the chosen category.

### How to Play
Run the Script: Execute hangman.py to start the game.

Choose a Category: Select a category from the list to get a word related to that category.

Guess the Word:

Enter letters to guess the word one letter at a time.

You can also guess the entire word if you think you know it.

Limited Attempts: You have 6 attempts to guess the word correctly.

Scoring:

Successfully guessing the word will display your score.

Failing to guess the word will reveal the correct word.

## Requirements
Python 3.x: Ensure you have Python 3.x installed on your system.

Installation
## Clone the Repository:

git clone https://github.com/BADUGU-SRICHETAN/hang-man.git
cd hangman
Install Python: Make sure Python 3.x is installed on your system. You can download it from the official Python website.

Running the Game
## Run the script using Python:

python hangman.py
Example Gameplay

Choose a category:
1. Programming
2. Animals
3. Countries
4. Fruits
5. Vegetables
6. Colors
7. Sports
8. Music
9. Movies
10. Books
...
Enter the number of your choice: 1

Welcome to Hangman!
Category: Programming
Guess the word:  _ _ _ _ _ _ 

Enter a letter or guess the entire word: p
Good job! 'p' is in the word.
Current word:  p _ _ _ _ _ 

...

Congratulations! You guessed the word: python
Your score: 30
## Game Design
The Hangman game is designed with a set of predefined stages representing the hangman. Each incorrect guess leads to the next stage being displayed, adding a limb to the hangman until all limbs are displayed and the game is lost. The player can guess letters or the entire word, with each correct guess revealing the letters in their correct positions.

Code Overview
Import Statements
python
import random
Display Hangman Function
python
def display_hangman(attempts):
    stages = [
        ''' 
           ------ 
           |    | 
           |    O 
           |   /|\\ 
           |   / \\ 
           | 
        --------- 
        ''',  # 0 attempts left
        #... Other stages
    ]
    return stages[attempts]
## Main Game Logic
python
def hangman():
    categories = {
        "Programming": ["python", "javascript", ...],
        "Animals": ["elephant", "giraffe", ...],
        #... Other categories
    }

    print("Choose a category:")
    for i, category in enumerate(categories.keys(), start=1):
        print(f"{i}. {category}")
    category_choice = input("Enter the number of your choice: ")

    #... Remaining game logic
Contribution
Contributions are welcome! Feel free to fork the repository, make improvements, and create pull requests.
