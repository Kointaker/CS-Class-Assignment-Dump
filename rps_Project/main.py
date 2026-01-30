import random

choices = ['rock', 'paper', 'scissors']

user = input("Enter rock, paper, or scissors: ").strip().lower()
computer = random.choice(choices)

print("You chose:", user)
print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == 'rock' and computer == 'scissors') or \
     (user == 'paper' and computer == 'rock') or \
     (user == 'scissors' and computer == 'paper'):
    print("You win!")
elif user in choices:
    print("You lose!")
else:
    print("Invalid input.")


