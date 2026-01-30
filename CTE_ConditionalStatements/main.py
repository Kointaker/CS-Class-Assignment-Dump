# Letter Grade Calculator

# This program allows a user to input a number grade (0-100) and will
# output the letter grade version

try:
    # Get user input
    grade_input = input("Enter a numeric grade (0-100): ")
    grade = float(grade_input)

    # Validate range
    if grade < 0 or grade > 100:
        print("Error: Grade must be between 0 and 100.")
    else:
        # Determine letter grade
        if grade >= 90:
            letter_grade = 'A'
        elif grade >= 80:
            letter_grade = 'B'
        elif grade >= 70:
            letter_grade = 'C'
        elif grade >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'

        # Output the result
        print(f"The letter grade for {grade} is {letter_grade}.")

except ValueError:
    print("Error: Please enter a valid numeric grade.")
