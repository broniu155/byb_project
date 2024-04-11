#----- Award program -------#

""" Program that determines the award 
    a person competing in a triathlon
"""

#------- Main code ---------#

#Define the variables for sports

swim_m = int(input("Enter swim time in minutes:"))
cycle_m = int(input("Enter cycle time in minutes:"))
run_m = int(input("Enter run time in minutes:"))

# sum all of the times and output result

total = sum([swim_m,cycle_m,run_m])
print("Total time of Triatlon is:",total)
 
 # set the condition for receiving the award
 
if (total <= 100):
     print("Provincial colours")
elif (total > 100) and (total <= 105):
     print("Provincial half colours")
elif (total > 105) and (total <= 110):
     print("Provincial scroll")
else:
     print("No award")
     