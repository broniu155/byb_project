"""
Program Name - whily.py

Author: Tomasz Bronewicz
Latest Version: 1.0
Date: 14/03/2024

Changes: 
v1.0 - Initial version - Tomasz Broniewicz

============Description===========

Program that continually asks the user
to enter a number

===================================
"""

# Define the variable for that is provided by user

int_num = int(input("Enter the integer value: "))

# Define variables for count input and sum
count = 0
total_sum = 0 # Default state for sum  variable as unable to use sum() for int

# While loop to ask user for number until condition is met

while int_num != -1:
    int_num = int(input("Enter another integer value: "))
    count += 1   # Increment count of 1 with every provided number
    total_sum += int_num  # Increment working as sum
if int_num == -1:
    avg = total_sum / count
    print(f"Average number of the entered number is: {avg} ")


#---------------------------------
# *Additional comments for tutor:
# I had to google the solution for the workaround for sum()

  
    