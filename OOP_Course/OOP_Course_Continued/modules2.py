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












class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
    
        self.flavors = ["Vanilla", "Strawberry", "Chocolate", "Banana", "Coco", "Blueberry", "Oreo"]
    
    def list_flavors(self):
        print(f"\nOur flavors are: {self.flavors}")













class Administrator(User):
    def __init__(self, first_name, last_name, id, ethnicity, wealth):
        super().__init__(first_name, last_name, id, ethnicity, wealth)

        self.privileges = Privileges()









class Privileges:
    def __init__(self):
    
        self.privileges = ["Can add post", "Can delete post", "Can ban user", "Can spawn admin items", "Can use invincibility", "Can use admin sword"]
    
    def show_privileges(self):
        print(f"\nThe privileges that admin users have are: {self.privileges}")











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


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"\nThe battery size of this car is: {self.battery_size}")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"\nThis car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
        

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = Battery()


    