# Josh
grades = []


def gpa_calc(grades):
    gpa = 0
    total = 0
    for i in grades:
        if (i == "A" or i == "A+"):
            gpa += 4.0
            total += 1
        elif i == "A-":
            gpa += 3.7
            total += 1
        elif i == "B+":
            gpa += 3.3
            total += 1
        elif i == "B":
            gpa += 3.0
            total += 1
        elif i == "B-":
            gpa += 2.7
            total += 1
        elif i == "C+":
            gpa += 2.3
            total += 1
        elif i == "C":
            gpa += 2.0
            total += 1
        elif i == "C-":
            gpa += 1.7
            total += 1
        elif i == "D+":
            gpa += 1.3
            total += 1
        elif i == "D":
            gpa += 1.0
            total += 1
        elif i == "F":
            gpa += 0.0
            total += 1
        else:
            print("Invalid grade")
     
    return gpa / total









user = int(input("How many grades are you putting in"))

for i in range(user):
    i+=1
    gr = input(f"Enter letter grade {i}").upper()
    grades.append(gr)


print(gpa_calc(grades))

