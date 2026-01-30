# MadLibs Generator
import time
from tqdm import tqdm

print("Welcome to MadLibs :)")

name = input("Whats your name? ")

age = int(input("Whats your age? "))

if age < 18:
    #DiddyLibs
    print("A minor I see\n")
    for i in tqdm(range(250), desc="Booting", ascii=False, ncols=75):
        time.sleep(0.004)
    print("\n")
    
    # DiddyLibs input prompts

    adjective1 = input("Enter a spicy adjective: ")
    body_part = input("Enter a body part: ")
    verb_past = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    adjective2 = input("Enter another provocative adjective: ")
    item = input("Enter a sus item: ")
    verb = input("Enter a verb: ")
    exclamation = input("Enter a flirty exclamation: ")
    drink = input("Enter a type of drink: ")
    celebrity = input("Enter a celebrity: ")


    thing = f"""
DiddyLibs:
Last night, I went to a {adjective1} party and couldn't believe my eyes when someone showed off their {body_part}. 
They {verb_past} right in the middle of the {place}, making everyone stare. 
The atmosphere was so {adjective2} that I spilled my {item} all over the floor. 
Suddenly, someone started to {verb} and everyone shouted, "{exclamation}!" 
We sipped on {drink} and even caught a glimpse of {celebrity} sneaking out the back.
"""
    print(thing)

# Normal MadLibs
else:
    zooname = input("Enter the name of the zoo: ")
    adjective1 = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb_past = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    adjective2 = input("Enter another adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    exclamation = input("Enter an exclamation: ")
    food = input("Enter a food: ")
    celebrity = input("Enter a celebrity: ")


    thing = f"""
Today I went to the {zooname} and saw a(n) {adjective1} {animal}. 
It {verb_past} right in front of me! I couldn’t believe it, so I ran to the {place} to tell my friend. 
The zoo was so {adjective2} that I almost dropped my {noun}. 
Suddenly, the animal started to {verb} and everyone shouted, 
"{exclamation}!" Afterward, we ate some {food} and even saw {celebrity} walking by.
"""
    
    print(thing)