import random
# 9-13. Dice: Make a class Die with one attribute called sides, which has a
# default value of 6. Write a method called roll_die() that prints a random num-
# ber between 1 and the number of sides the die has. Make a 6-sided die and
# roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
class Die:
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        print(random.randint(1, 6))

sided6 = Die(6)
sided10 = Die(10)
sided20 = Die(20)

for i in range(10):
    sided6.roll_die()
    sided10.roll_die()
    sided20.roll_die()




# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list and print a message saying that
# any ticket matching these 4 numbers or letters wins a prize.

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "L", "M", "N", "O", "P"]


print(f"Any ticket that mathing these 4 numbers or letters wins: ")
for i in range(4):
    x = random.randint(0, 14)
    print(L[x])




# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
# a loop that keeps pulling numbers until your ticket wins. Print a message report-
# ing how many times the loop had to run to give you a winning ticket.