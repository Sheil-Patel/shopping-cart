# shopping_cart.py

from datetime import datetime
import csv
import os
import pandas as pd

#products = [
#    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}]

def to_usd(my_price):
        return f"${my_price:,.2f}" #> $12,000.71
        
def human_friendly_timestamp(now):
    current_time = now.strftime("%H:%M:%S")
    d3 = now.strftime("%m/%d/%y")
    output = f"Checkout On: {d3} at {current_time}"
    print(output)
    return output

def print_receipt(time, subtotal,tax_amount,final_total):
    print("-------------------------------------------")
    print("Kroger Grocery Store")
    print("1-215-677-0952")
    print("www.Kroger.com")
    print("-------------------------------------------")
    print(time)
    print("-------------------------------------------")
    print("SELECTED PRODUCTS:")
    print("-------------------------------------------")
    print("SUBTOTAL:" + str(to_usd(subtotal)))
    print("TAX: " + str(to_usd(tax_amount)))
    print("TOTAL: " + str(to_usd(final_total)))
    print("-------------------------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
    print("-------------------------------------------")

def find_subtotal(selected_ids, products):
    subtotal = 0.0
    for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)] #> Filters through list to check for matching product ID
        matching_product = matching_products[0] #> Changes list datatype to dictionary datatype
        subtotal = subtotal + matching_product["price"]
    return subtotal

def find_product(selected_ids, products):
    for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)] #> Filters through list to check for matching product ID
        matching_product = matching_products[0] #> Changes list datatype to dictionary datatype
        print(" . . . " + matching_product["name"] + " " +"(" +str(to_usd(matching_product["price"]))+ ")") #> 
    return matching_product

def tax_calculation(subtotal):
    taxrate = .0875
    tax_amount = taxrate * subtotal
    return tax_amount

def final_total_function(subtotal, tax_amount):
    final_total = subtotal + tax_amount
    return final_total
  

products = []

if __name__ == "__main__":
    #Reading CSV
    stats = pd.read_csv("Data/products.csv")
    for index, row in stats.iterrows():
        p={}
        p["id"] = row["id"]
        p["name"] = row["name"]
        p["department"] = row["department"]
        p["aisle"] = row["aisle"]
        p["price"] = float(row["price"])
        products.append(p)
    #INFO CAPTURE / INPUT
    selected_ids = []

    while True:
        hello = False
        selected_id = input("Please input a product identifier: ") #> stored as string
        if selected_id == "DONE" or selected_id == "done":
            break
        else:
            for p in products:
                if str(p["id"]) == selected_id:
                    hello = True
        if hello == False:
            print("Hey, are you sure that product identifier is correct? Please try again!")        
        else:
            selected_ids.append(selected_id)

    if len(selected_ids) == 0:
        print("You did not put in any valid identifiers: Thank you for using my program")
        exit()
    #Pulling Datetime 
    now = datetime.now()


    #Info Display / Output Header

    time = human_friendly_timestamp(now)

    find_product(selected_ids, products)
    
    subtotal = find_subtotal(selected_ids, products)

    tax_amount = tax_calculation(subtotal)

    final_total = final_total_function(subtotal, tax_amount)

    print_receipt(time ,subtotal,tax_amount,final_total)