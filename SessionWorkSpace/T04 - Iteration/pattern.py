"""
Program Name - pattern.py

Author: Tomasz Bronewicz
Latest Version: 1.0
Date: 14/03/2024

Changes: 
v1.0 - Initial version - Tomasz Broniewicz

============Description===========

Program that output the certain patern showed
in Task using if-else statement with for loop

===================================
"""


# Define the variable for star symbol

stars ="*"

# Create for loop to print star symbol
 

for i in range(1,10):
    print(stars)
    stars = stars + "*" # add star with each iteration
    if i >= 5:
        stars = stars[:-2]   # -2 Index as every loop ads "*"      

        
        

 
