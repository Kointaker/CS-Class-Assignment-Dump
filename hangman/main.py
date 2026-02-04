# hangman
# your name, the date

##### import statements


##### functions

## welcome message & game rules
# parameters: maximum incorrect tries, length of secret word
# return: nothing
def print_game_rules():
    pass


## get user letter
# ask user to enter a single alphabetical letter
# parameters: None
# return: a single letter guess
def get_user_letter():
    pass


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


##### main program
### variables



### game loop

# change this later to a random word using 
# random.choice() and a list of words
word = "computer"

# variable to store the underscores (_) and correct letters
# that the user has guessed
blank_word = []

# add an _ for every letter in the WORD
for letter in word:
    blank_word.append('_')

# print the blank_word variable but not as a list
print(" ".join(blank_word))
