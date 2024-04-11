"""
Program Name - cafe.py

Author: Tomasz Bronewicz
Latest Version: 1.0
Date: 20/03/2024

Changes: 
v1.0 - Initial version - Tomasz Broniewicz

============Description===========
Program that will help to run coffeshop.
Summarise all of the items that are on menu
to show the value of the stock
===================================
"""

#===================================

# Function for menu list

#===================================
def list_items():
    menu_item = ["Tea","Coffee","Chocolate","Brownie","Cookie"]
    return menu_item

#===================================

# Function for stock dictionary for each item

#===================================
def dict_stock():
    stock = {
        "Tea": 60,
        "Coffee": 1000,
        "Chocolate": 64,
        "Brownie": 7,
        "Cookie": 30
    }
    return stock

#===================================

# Function for price dictionary for each item

#===================================

def dict_price():
    price = {
        "Tea": 1.30,
        "Coffee": 2.10,
        "Chocolate": 1.60,
        "Brownie": 3.15,
        "Cookie": 0.90
    }
    return price

#===================================

# Function for calculating all of the items
# to get the value of the products in stock

#===================================

def total_status(menu,prices,stock):
    
    total_stock_value = 0 # new value for total as float is not iterable
      
         
    for item in menu:
       item_value = (stock[item] * prices[item]) # calculate each item in stock
       print(f"We currently have {item} priced at {prices[item]:.2f}£ " 
             f"which is overall cost of:{(item_value):.2f}£")
       total_stock_value += item_value # loop through each item_value
    return total_stock_value 
           
           
# Calling the functions
          
menu = list_items()    
prices = dict_price()
stock = dict_stock()  
total_stock_value = total_status(menu,prices,stock)
print(f"Total stock value : {(total_stock_value):.2f}£")


"""
Coments for mentor:

I am not sure but I would like to print the below statement corectly to avoid f""
       print(f"We currently have {item} priced at {prices[item]:.2f}£ " 
             f"which is overall cost of:{(item_value):.2f}£")

I have been told that this is not efficient and problematic for 
interpolation so what is the best idea to that?

I have tried this
       print(f"We currently have {item} priced at {prices[item]:.2f}£ " 
             "which is overall cost of:{(item_value):.2f}£")

but I have error: unterminated string literal 
"""