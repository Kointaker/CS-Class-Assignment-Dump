# Contact List Starter Code
# Your name, the date

### import satements
import time
### functions




## add contact - adds a new key, value dictionary
# to the contacts dictionary
# parameters: a dictionary
# return: nothing
def add_contact(contacts):
    
    full_name = input("Enter contact's full name: ")
    phone_number = int(input("Enter contact's phone number: "))
    email = input("Enter contact's email address: ")
    address = input("Enter contact's home address: ")
    birthday = input("Enter contact's birthday: ")
    notes = input("Enter any notes about the contact: ")
    contact_name = input("Enter a name/nickname for the contact: ")
    # add new key, value to contacts dictionary
    
    contacts[f"{contact_name}"] = {"full_name": full_name, "phone_number": phone_number, "email": email, "address": address, "birthday": birthday, "notes": notes}



## delete contact - deletes contact from dictionary
# parameters: a dictionary
# return: nothing
def remove_contact(contacts):
    # test if nickname is in dictionary
    # if name is found, remove key, value
    # else, tell user contact is not found
    remove = input("Enter the name/nickname of the contact you want to remove: ")
    
    if remove in contacts:
        del contacts[remove]
    else:
        print("Contact not found.")




## show contact info
# print single contact from dictionary
# parameters: a dictionary
# return: nothing
def show_contact_info(contacts):
    # if name in dictionary,
    # print information about contact
    list_contacts(contacts)
    show = input("Enter the name/nickname of the contact info you want to see (case sensitive): ")
    print("Full Name:", contacts[show]["full_name"])
    print("Phone Number:",contacts[show]["phone_number"])
    print("Email:", contacts[show]["email"])
    print("Address:", contacts[show]["address"])
    print("Birthday:", contacts[show]["birthday"])
    print("Notes:", contacts[show]["notes"])



## show contact phone number
# print phone number for single contact
# parameters: a dictionary
# return: nothing
def show_phone_number(contacts):
    # if name in dictionary
    # print phone number of contact
    list_contacts(contacts)
    show = input("Enter the name/nickname of the contact you want to see the phone number of (case sensitive): ")
    print(contacts[show]["phone_number"])




def list_contacts(contacts):
    # print list of all contact names/nicknames in dictionary
    for value in contacts:
        print(value)


### main program

## variables

# contact list dictionary
# nickname keys MUST be unique!
# what should be in contacts:
# First and Last Name
# Personal, Work Telephone Numbers
# Email Address
# Home Address
# Birthday
# Notes
# Profile Picture
contacts = {
"Josh":{
    "full_name": "Josh Smith",
    "phone_number": 9786414591,
    "email": "Kointaker9@gmail.com",
    "address": "336 Haverhill",
    "birthday": "June 25 2008",
    "notes": "Best friend since 3rd grade"

}

}

while True:
    time.sleep(1)
    print("\n\n\n")
    print("What would you like to do?")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Show contact info")
    print("4. Show contact phone number")
    print("5. List available contacts")
    print("6. Exit")
    choice = int(input("Enter the number of your choice: "))
    
    if choice == 1:
        print("")
        add_contact(contacts)
    elif choice == 2:
        print("")
        remove_contact(contacts)
    elif choice == 3:
        print("")
        show_contact_info(contacts)
    elif choice == 4:
        print("")
        show_phone_number(contacts)
    elif choice == 5:
        print("")
        list_contacts(contacts)
    elif choice == 6:
        break
    elif choice == 10:
        print("")
        print(contacts)
    else:
        print("Invalid choice. Please try again.")


