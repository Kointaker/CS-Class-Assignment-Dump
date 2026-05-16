from user import User
class Administrator(User):
    def __init__(self, first_name, last_name, id, ethnicity, wealth):
        super().__init__(first_name, last_name, id, ethnicity, wealth)

        self.privileges = Privileges()









class Privileges:
    def __init__(self):
    
        self.privileges = ["Can add post", "Can delete post", "Can ban user", "Can spawn admin items", "Can use invincibility", "Can use admin sword"]
    
    def show_privileges(self):
        print(f"\nThe privileges that admin users have are: {self.privileges}")




