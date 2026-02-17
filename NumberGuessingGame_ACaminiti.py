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

attempts = 5

current_attempts = attempts - 1



# ATTEMPTS/MAIN PART

int(input("Enter A Number: "))


i = 5

while i < 5: 
 print()
 if i == 5:
  break
 i += 1


# 

 if attempts >= 5:
  print("You are out of attempts :(")
  
