# Challenge 3 Starter Code
numbers = []

for x in range(1, 6):
    user_input = int(input("Enter Your Numbers: "))

values = numbers

# ERROR HANDLING 
try:
 numbers = int("hello")
except ValueError as e:
 print(f"Error: {e}")

#  print (values + values + values + values + values) / 5