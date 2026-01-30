# Joshua Ferreira, 10/9/2025
# functions: text adventure project starter code

### imports
import time
# global variables
has_key = False
jump_count = 0

### functions
def welcome():
    print("*" * 20)
    print("Welcome to the game!")
    print("*" * 20)
    print()

def diddy_room():
    print("You got oiled up!")
    x = print(input("\n wanna do some more? y/n")).lower()
    if x == "y":
        print("You got oiled up!" * 50)
        diddy_room()
    elif x == "n":
        spawn_room()
    else:
        print("teleporting to spawn room")
        time.sleep(1)
        spawn_room()


def liams_basement():
    print("What do you want to do? ")
    spawn_room()


def dishas_house():
    print("Who do you want to see: ")
    print("""
1: Disha
2: Diya
3: Daksh

""")



def spawn_room():
    global has_key
    global jump_count

    print("\nYou are in a room.")
    print("There is an open door to another room\nand a locked door.")

    print("\nWhat do you want to do?")
    print("A - Jump in place.")
    print("B - Enter the unlocked room.")
    print("C - Open the locked door.")
    print("D - Go to diddy's room.")
    print("E - Go to Liam's basement.")
    print("F - Go to Disha's house.")

    choice = input(": ").lower()
    print()

    if choice == "a":
        jump_count += 1
        print(f"You have jumped {jump_count} time(s).")
        spawn_room()
    elif choice == "b":
        key_room()
    elif choice == "c":
        if has_key:
            print("You unlock the locked door with the rusted key.")
            main_hall()
        else:
            print("The door is locked...")
            spawn_room()
    
    elif choice == "d":
        diddy_room()

    elif choice == "e":
        liams_basement()

    elif choice == "f":
        dishas_house()
    
    
    else:
        print("Please choose an option.")
        spawn_room()

def key_room():
    global has_key
    global jump_count

    print("\nYou are in a room with no windows\nwith only the door you just walked through.")
    if has_key:
        print("You are holding a warm rusted key.")
    else:
        print("You see a small rusted key on the floor.")

    print("\nWhat do you want to do?")
    print("A - Jump in place.")
    print("B - Enter the unlocked room.")
    if has_key == False:
        print("C - Pick up the rusted key.")

    choice = input(": ").lower()
    print()

    if choice == "a":
        jump_count += 1
        print(f"\nYou have jumped {jump_count} time(s).")
        key_room()
    elif choice == "b":
        spawn_room()
    elif choice == "c" and has_key == False:
        print("You pick up the rusted key. It feels warm...")
        has_key = True
        key_room()

def main_hall():
    global jump_count

    print("You are in the main hallway...")

    print("\nWhat do you want to do?")
    print("A - Jump in place.")

    choice = input(": ").lower()
    print()

    if choice == "a":
        jump_count += 1
        print(f"\nYou have jumped {jump_count} time(s).")
        main_hall()

### main
welcome()
spawn_room()
#main_hall()



