print("Welcome to the grade checker program!")
while True:
    marks = float(input("Enter your marks (0-100): "))
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "Fail"
    print(f"Your grade is {grade}")
    again = input("Do you want to check the grade for another marks?: ")
    if again.lower() != "yes":
        print("Thank you")
        break
