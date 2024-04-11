"""
Program Name - dob_task.py

Author: Tomasz Bronewicz
Latest Version: 1.0
Date: 22/03/2024

Changes: 
v1.0 - Initial version - Tomasz Broniewicz

============Description===========

Program that will that help to record
and mantaint he student register for
exam venue

===================================
"""
#==================================

# Function to add student to register

#===================================
 
def add_register():
   
    num_user = int(input("Enter how many users would you like to register: "))
    user_list = [] 
    
    for i in range(num_user):
        user_id = input((f"Enter {i + 1} from {num_user} user ID to register: "))
        user_list.append(user_id)
    return user_list

#==============================

# Function to import the data to txt file

#===============================

def reg_form(content):
    
#    content = (" ").join(content)
    
    with open ("reg_form.txt","a+") as f:
        for id in content:
            f.write(id  +" ........................................................." + "\n")
    
# Calling the functions
    
id_list = add_register()
complete_form = reg_form(id_list)

    
