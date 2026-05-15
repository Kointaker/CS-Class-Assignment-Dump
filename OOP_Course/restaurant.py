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
            self.number_served = 0
            
        def describe_restaurant(self):
            print(f"Restaurant name: {self.restaurant_name}")
            print(f"Cuisine type: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"{self.restaurant_name} is now open!")

        def increment_number_served(self, x):
            self.number_served += x
        
        def set_number_served(self, x):
            self.number_served = x





        
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
            self.login_attempts = 0

        def increment_login_attempts(self):
            self.login_attempts += 1

        def reset_login_attempts(self):
            self.login_attempts = 0
        
        def describe_user(self):
            print(f"""
User Information: {self.first_name} {self.last_name}
Id: {self.id}
Ethnicity: {self.ethnicity}
Wealth Class: {self.wealth}


""")

        def greet_user(self):
            print(f"Hello {self.first_name}, welcome to our restaurant, we have great food that you would enjoy. \nYour id for the all-you-can-eat is {self.id}, enjoy!\n\n")


    Josh = User("Joshua", "Ferreira", 12811068, "Dominican", "Upper-Class")
    Josh.describe_user()
    Josh.greet_user()
    
    Cliff = User("Clifford", "Ashbrook", 11112211, "Japanese", "Ultra-Wealth")
    Cliff.describe_user()
    Cliff.greet_user()

    Andrew = User("Andrew", "Leung", 11111111, "African", "Hyper-Wealth")
    Andrew.describe_user()
    Andrew.greet_user()






#     9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day of
# business.

    restaurant = Restaurant("Bunger Bagels", "Japanese")
    print(f"\nNumber served at {restaurant.restaurant_name}: {restaurant.number_served}")
    restaurant.number_served = 10
    print(f"\nNumber served at {restaurant.restaurant_name}: {restaurant.number_served}")
    restaurant.increment_number_served(51)
    print(f"\nNumber served at {restaurant.restaurant_name}: {restaurant.number_served}")
    restaurant.set_number_served(3)
    print(f"\nWhoops, we counted wrong, we actually served {restaurant.number_served} people today!!")



# 9-5. Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.


    jj = User("Liam", "Mackenzie", 677677, "White Wite", "Ultra High")
    print(f"\n\n Starting Login attempts: {jj.login_attempts}")
    jj.increment_login_attempts()
    jj.increment_login_attempts()
    jj.increment_login_attempts()
    print(f"\nI tried logging in 3 times, my login attempts are now: {jj.login_attempts}")
    jj.reset_login_attempts()
    print(f"Login attempts were reset, attempts is now at: {jj.login_attempts}")






#     9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type):
            super().__init__(restaurant_name, cuisine_type)
        
            self.flavors = ["Vanilla", "Strawberry", "Chocolate", "Banana", "Coco", "Blueberry", "Oreo"]
        
        def list_flavors(self):
            print(f"\nOur flavors are: {self.flavors}")
        
        
    Josh = IceCreamStand("Josh's Ice Cream", "Ice Cream")

    Josh.list_flavors()






# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.


    class Administrator(User):
        def __init__(self, first_name, last_name, id, ethnicity, wealth):
            super().__init__(first_name, last_name, id, ethnicity, wealth)

            self.privileges = Privileges()



            




    

        







# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.


    class Privileges:
        def __init__(self):
        
            self.privileges = ["Can add post", "Can delete post", "Can ban user", "Can spawn admin items", "Can use invincibility", "Can use admin sword"]
        
        def show_privileges(self):
            print(f"\nThe privileges that admin users have are: {self.privileges}")

   
    Landon = Administrator("Landon", "Terry", 116644, "White", "Ultra Wealthy")
    Landon.privileges.show_privileges()






# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 65 if it isn’t already. Make
# an electric car with a default battery size, call get_range() once, and then
# call get_range() a second time after upgrading the battery. You should see an
# increase in the car’s range.

    class Car:
        def __init__(self, make, model, year):
    
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0
            
        def get_descriptive_name(self):
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()
        
        def read_odometer(self):
            print(f"This car has {self.odometer_reading} miles on it.")
        
        def update_odometer(self, mileage):
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")
        
        def increment_odometer(self, miles):
            self.odometer_reading += miles
    
    
    class ElectricCar(Car):
        def __init__(self, make, model, year):
            super().__init__(make, model, year)
   
   
   
    my_leaf = ElectricCar("nissan", "leaf", 2024)
    print("\n", my_leaf.get_descriptive_name())






























if __name__ == "__main__":
    main()