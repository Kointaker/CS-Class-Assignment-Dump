# Basic game function expectations:
# 
# -If a guess is correct, fill in the letter
# -If a guess is incorrect, fill in the hangman
# -Users have 6 incorrect guesses before 
# -If user loses, show game over screen, show them the word, and allow them to try again
# -If user wins, show win screen, and allow them to try againimport time

import random
import time
# From other file
from functions import display_figure, collect_guess


# Variables/to start:
starter_list = ["hello", "goodbye", "good", "bad", "happy", "sad", "content"]
word = []
choice = starter_list[random.randint(0, 6)]
for i in list(choice):
    word.append(i)
print(word)
bad_guesses = 0





def main():
    print("Welcome to hangman! You will be allowed to guess incorectly 6 times, after that, you lose!")
    time.sleep(1)
    collect_guess()




if __name__ == "__main__":
    main()
