"""
Program Name - holiday.py

Author: Tomasz Bronewicz
Latest Version: 1.0
Date: 15/03/2024

Changes: 
v1.0 - Initial version - Tomasz Broniewicz

============Description===========

Program to calculate a user's total holiday cost,
which includes the plane cost, hotel cost,
and car-rental cost

===================================
"""

#==================================

# function for option to choose the flight 

#===================================


def city_choose():   
    city_list = ["Amsterdam","Tokio","London","Toronto",
           "Berlin","Quit"]

    
    print("Airport list")
    for city in city_list:
        print(city)
    return city_list  
    

choice = None # Define variable for choice to default state

# Assign the city_list from function to variable outside the scope of the function
city_list = city_choose() 

 #logic for assign choice to the the correct value of flight       
while choice not in city_list:
    choice = input("Enter city name from above list to choose flight: ")
    if choice == city_list[0]:
        choice = round(float(120.23),2)
        print(f"You choose Amsterdam! Flight cost is {choice}£") 
        break
    if choice == city_list[1]:
        choice = round(float(720.25),2)
        print(f"You choose Tokio! Flight cost is {choice}£") 
        break
    if choice == city_list[2]:
        choice = round(float(130.25),2)
        print(f"You choose London! Flight cost is {choice}£") 
        break
    if choice == city_list[3]:
        choice = round(float(540.32),2)
        print(f"You choose Toronto! Flight cost is {choice}£") 
        break
    if choice == city_list[4]:
        choice = round(float(140.32),2)
        print(f"You choose Berlin! Flight cost is {choice}£") 
        break
    if choice == city_list[5]:
        print(f" We are sad you are not choosing our service, Goodbye!")
        break
        
             

#==================================

# Definition of main variables

#==================================

city_flight = round(float(choice),2) # automatic assigment from user choice
num_nights = round(float(input("Enter number of nights you wish to stay in hotel: ")),2)
rental_days = round(float(input("Enter number of days that you wish to rent a car: ")),2)


#========================================

# Function for calculating the hotel_cost

#========================================

def hotel_cost(num_nights):
    c_per_night = 200
    x = c_per_night * num_nights
    return x

print(f"Total cost of stay in hotel: {hotel_cost(num_nights)}£")

hotel = hotel_cost(num_nights)

#========================================

# Function for calculating the car rental

#========================================

def car_rental(rental_days):
    daily_cost = 75
    y = daily_cost * rental_days
    return y

print(f"Total cost of car rental: {car_rental(rental_days)}£")
    
car = car_rental(rental_days)

 #=======================================
 
 # Function to sumarize all of the cost of the journey
 
 #=======================================
 
def holiday_cost(car,hotel,city_flight):
    total = car + hotel + city_flight
    return total
 
print(f"Total price of you holiday is {round(holiday_cost(car,hotel,city_flight),2)}£")
        