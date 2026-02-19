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



attempts = 5

current_attempts = attempts - 1


# ATTEMPTS WHILE LOOP

user_guess = int(input("Enter A Number: "))

while(user_guess): 
 print(current_attempts)
 break
else:
 print("You have ran out of atttempts :(")

#HIGHER/LOWER PART

if user_guess < actual_number:
 print("lower")

else:
 print("higher")



 print(attempts)

 