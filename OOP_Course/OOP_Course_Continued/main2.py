
from modules2 import Restaurant
from user import User
from admin import Administrator, Privileges


#     9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod-
# ule. Make a separate file that imports Restaurant. Make a Restaurant instance,
# and call one of Restaurant’s methods to show that the import statement is work-
# ing properly.

new = Restaurant("Super-Foods", "American Food")
print(new.number_served)
new.describe_restaurant()




# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
# the classes User, Privileges, and Admin in one module. Create a separate file,
# make an Admin instance, and call show_privileges() to show that everything is
# working correctly.

josh = Administrator("Joshua", "Ferreira", 123123, "Dominican", "Ultra-Wealth")
josh.privileges.show_privileges()






# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.


Landon = Administrator("Landon", "Terry", 132123, "White", "Rich")
Landon.privileges.show_privileges()

