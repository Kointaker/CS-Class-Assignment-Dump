# Basic game function expectations:
# 
# -If a guess is correct, fill in the letter
# -If a guess is incorrect, fill in the hangman
# -Users have 6 incorrect guesses before 
# -If user loses, show game over screen, show them the word, and allow them to try again
# -If user wins, show win screen, and allow them to try againimport time









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






