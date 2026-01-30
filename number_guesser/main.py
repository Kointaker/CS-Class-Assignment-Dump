# Guess the Number Game
# Joshua Ferreira

# Requirements:

# -User must be able to input their guesses
# -After getting user input, code should tell user if it's wrong or right
# -Code should run right away
# -Code should be simply made
# -Code should have an obvious finish point

## Problem Statement

# Develop a software game that allows users to enter their number guess, and show whether the user got it right or wrong, giving the user simple fun.

min = 0
max = 10
tries = 0

### import statements ###

import random
### user defined functions ###


# returns the user's validated guess
def get_user_num():
    while True:
        x = input("Enter your guess here: ")
        try:
            attempt = int(x)
            break
        except ValueError:
            print("Enter an integer next time")
    
    return attempt

# check_num takes in 2 parameters and 
# either calls win_message or prints hints
def check_num(win, count, attempt):
    if attempt == win:
        win_message(count)
        quit()
    elif attempt > win:
        print("Too high!")
    elif attempt < win:
        print("Too low!")
    
def win_message(count):
    print(f"Yay! You won after {count} attempts.")


def lose_message(win, count):
    print(f"You lost! :( The number was {win}.")

### main program ###
def main():
    

    tries = 4
    win = random.randint(min, max)
    count = 0
    for i in range(tries):
        count += 1
        
        check_num(win, count, get_user_num())

    print(lose_message(win, count))

    



if __name__ == "__main__":
    main()