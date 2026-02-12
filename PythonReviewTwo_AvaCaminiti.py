age = int(input("Enter your age: "))

if age >= 18: 
    print("You are over 18!!")

else: 
    print("You are not over 18 :(")




menu = int(input("Choose option: "))

match menu:
    case 1:
        print("Start")
    case 2:
        print("Settings")
    case 3:
        print("Exit")
    case _:
        print("Invalid choice")
    