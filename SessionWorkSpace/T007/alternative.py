"""
Program Name - alternative.py

Author: Tomasz Bronewicz
Latest Version: 1.0
Date: 19/03/2024

Changes: 
v1.0 - Initial version - Tomasz Broniewicz

============Description===========

Program that reads in a string and makes each alternate
character into an upper case character and each alternate
character a lower case character

e.g The string "Hello World" would become "HeLlO WoRlD"

===================================
"""

#===================================

# Function for alternating characters

#===================================
def alternate_char(string):

    new_string = "" # Define variable for new string
    i = 0  # Define variable for index
    
    
    # loop for checking if character is even or odd
    for char in string:
        if i % 2 == 0:
            char = char.upper()
        else:
            char = char.lower()
        i += 1   
        new_string += char
    return new_string # returning new string

#===================================

# Function for alternating original characters to transpose
# each individual sentance word to upper and lower case

#===================================
def alternate_word(string):

    new_word_string =""
    i = 0
    
    new_word = string.split(" ") # split each word to the item in the list
    
    # loop for checking if word is even or odd
    for word in new_word:
        if i % 2 == 0:
            word = word.upper()
        else:
            word = word.lower()
        i += 1
        new_word_string += word + " "
    return new_word_string
 

og_string = input("Enter the string: ") 

# calling functions
result = alternate_char(og_string)
print(result)     

full_word = alternate_word(og_string)    
print(full_word)