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

