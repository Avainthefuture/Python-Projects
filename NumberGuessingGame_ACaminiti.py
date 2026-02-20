import random

# Name: Ava Caminiti
# Version: 1.0
# Explanation: This program will have a user guess a number until time runs out. 
# Sources Used: W3 Schools, Google Classroom, Other Projects. 


# INTRODUCTION

print("Enter Your Name: ")
name = input()

print(f"Hello {name} Welcome To Number Guessing Game!!! Today You Will Have 5 Attempts To Guess A Number. If You Use All 5 Attempts Then You Will Run Of Time. Enjoy!!!")


# VARIABLES

random_number = random.randint(1, 100)

running = True

actual_number = random_number 

print(actual_number)


attempts = 5




# ATTEMPTS WHILE LOOP 



while running:
    user_guess = int(input("Enter A Number: "))
    # print(current_attempts)

    if user_guess < actual_number:
        print("higher")
        current_attempts -= 1
        continue


    elif user_guess > actual_number: 
        print("lower")
    else:
        print("you got it!!")
        
        continue




    


 