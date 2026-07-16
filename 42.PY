password = "Krishna Vamshi"
attempts = 3
while attempts > 0:
    entered = input("Enter password: ")
    if entered == password:
        print("Access granted")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Access denied")
        else:
            print(f"Wrong password. {attempts} attempt(s) left.")
