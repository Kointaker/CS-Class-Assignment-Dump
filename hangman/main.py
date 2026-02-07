# -If a guess is correct, fill in the letter
# -If a guess is incorrect, fill in the hangman
# -Users have 6 incorrect guesses before losing
# -If user loses, show game over screen, and show them the word
# -If user wins, say they win


##### import statements #####
import random
import time

##### functions #####



## welcome message & game rules
# parameters: maximum incorrect tries, length of secret word
# return: nothing
def print_game_rules():
    print("You get 6 wrong attempts, after that, you lose. Good luck!")
    time.sleep(1)

## get user letter
# ask user to enter a single alphabetical letter
# parameters: None
# return: a single letter guess
def get_user_letter():
    global guess
    while True:
        guess = input("Guess here: ").lower()
        if len(guess) == 1:
            break
        else:
            print("Hey! Input one word!")
    return guess

def check_guess(guess, incorrect_guesses):
    if guess not in lettered_word:
        incorrect_guesses += 1
        return incorrect_guesses
    else:
        for letter in lettered_word:
            if guess == letter:
                blank_word[lettered_word.index(letter)] = letter
                lettered_word[lettered_word.index(letter)] = '_'
        

            


    

## display hangman figure
# print the current graphic based on bad guesses
# parameters: current numer of incorrect bad_guesses
# return: nothing
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

# DEBUG test for display_figure()
# for x in range(7):
#     display_figure(x)
# remove above for loop before final version


##### main program #####
### variables ###



### game loop ###

# change this later to a random word using 
# random.choice() and a list of words
words = ["hello", "goodbye", "good", "bad", "content", "furious", "bombaclat"]
word = words[random.randint(0, 6)]
lettered_word = []
# variable to store the underscores (_) and correct letters
# that the user has guessed
blank_word = []
incorrect_guesses = 0
# add an _ for every letter in the WORD
# and split the word into a list of it's letters
for letter in word:
    blank_word.append('_')
    lettered_word.append(letter)









def main(incorrect_guesses):

    while True:
            
        # Dev view
        # print(f"Lettered word: {lettered_word}")
        
        
        get_user_letter()
        check_guess(guess, incorrect_guesses)

        # print the blank_word variable but not as a list
        print(" ".join(blank_word))
        display_figure(incorrect_guesses)
        print(f"Incorrect guesses: {incorrect_guesses}")
        # Dev view
        # print(f"Blank word: {blank_word}")
        print("\n\n")
        if incorrect_guesses == 6:
            print(f"Game over! The word was {word}.")
            break

        if "_" not in blank_word:
            print("Congrats! You win!")
            break

if __name__ == "__main__":
    main(incorrect_guesses)