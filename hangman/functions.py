# Functions

import random
import time


def display_figure(bad_guesses):
    hangmen = ["""
+------+
|
|
|
|
=========""","""
+------+
|      o
|
|
|
=========""","""
+------+
|      o
|      |
|
|
=========""","""
+------+
|      o
|     /|
|
|
=========""","""
+------+
|      o
|     /|\\
|
|
=========""","""
+------+
|      o
|     /|\\
|     /
|
=========""","""
+------+
|      o
|     /|\\
|     / \\
|
========="""]
    
    print(hangmen[bad_guesses])
    return



# Functions: Continued

# # Variables/to start:
# starter_list
# choice: Word in normal format
# word 
# bad_guesses 

def collect_guess():
    global guess
    while True:
        guess = input("Enter a letter for your guess: ").lower()
        
        if len(guess) == 1:
            break
        else:
            print("Hey! Only one letter!")
        


def check(guess):
    pass














def main():
    pass




while __name__ == "__main__":
    pass
