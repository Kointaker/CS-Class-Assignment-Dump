# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

def main():
        
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Restaurant name: {self.restaurant_name}")
            print(f"Cuisine type: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"{self.restaurant_name} is now open!")

    Michaels = Restaurant("Michaels", "Seafood")

    # Individually printing restaurant information
    print(Michaels.restaurant_name)
    print(Michaels.cuisine_type)
    print("\n")
    
    # Calling Restaurant methods
    Michaels.describe_restaurant()
    Michaels.open_restaurant()
    print("\n")

    # 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
    # different instances from the class, and call describe_restaurant() for each
    # instance.

    ava = Restaurant("Greek Pretzels", "Greek Food")
    michael = Restaurant("Cool Cuisine", "Cracker food")
    josh = Restaurant("Dominican Drive", "Dominican Cuisine")
    
    ava.describe_restaurant()
    michael.describe_restaurant()
    josh.describe_restaurant()
    print("\n")

    # 9-3. Users: Make a class called User. Create two attributes called first_name
    # and last_name, and then create several other attributes that are typically stored
    # in a user profile. Make a method called describe_user() that prints a summary
    # of the user’s information. Make another method called greet_user() that prints
    # a personalized greeting to the user.
    # Create several instances representing different users, and call both meth-
    # ods for each user.
    class User:
        def __init__(self, first_name, last_name, id, ethnicity, wealth):
            self.first_name = first_name
            self.last_name = last_name
            self.id = id
            self.ethnicity = ethnicity
            self.wealth = wealth

        def describe_user(self):
            print(f"""
User Information: {self.first_name} {self.last_name}
Id: {self.id}
Ethnicity: {self.ethnicity}
Wealth Class: {self.wealth}


""")


        def greet_user(self):
            print(f"Hello {self.first_name}, welcome to our restaurant, we have great food that you would enjoy. \nYour id for the all-you-can-eat is {self.id}, enjoy!")
            



    Josh = User("Joshua", "Ferreira", 12811068, "Dominican", "Upper-Class")
    Josh.describe_user()
    Josh.greet_user()
    
    Cliff = User("Clifford", "Ashbrook", 11112211, "Japanese", "Ultra-Wealth")
    Cliff.describe_user()
    Cliff.greet_user()

    Andrew = User("Andrew", "Leung", 11111111, "African", "Hyper-Wealth")
    Andrew.describe_user()
    Andrew.greet_user()





if __name__ == "__main__":
    main()