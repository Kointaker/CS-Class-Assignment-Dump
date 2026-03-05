# Contact List Starter Code
# Your name, the date

### import satements

### functions




## add contact - adds a new key, value dictionary
# to the contacts dictionary
# parameters: a dictionary
# return: nothing
def add_contact():
    
    full_name = input("Enter contact's full name: ")
    phone_number = input("Enter contact's phone number: ")
    email = input("Enter contact's email address: ")
    address = input("Enter contact's home address: ")
    birthday = input("Enter contact's birthday: ")
    notes = input("Enter any notes about the contact: ")
    contact_name = input("Enter a name/nickname for the contact: ")
    # add new key, value to contacts dictionary
    
    contacts[f"{contact_name}"] = [full_name, phone_number, email, address, birthday, notes]



## delete contact - deletes contact from dictionary
# parameters: a dictionary
# return: nothing
def remove_contact(dict):
    # test if nickname is in dictionary
    # if name is found, remove key, value
    # else, tell user contact is not found
    pass



## show contact info
# print single contact from dictionary
# parameters: a dictionary
# return: nothing
def show_contact_info():
    # if name in dictionary,
    # print information about contact
    pass



## show contact phone number
# print phone number for single contact
# parameters: a dictionary
# return: nothing
def show_phone_number():
    # if name in dictionary
    # print phone number of contact
    pass




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


}
add_contact()
print(contacts)



