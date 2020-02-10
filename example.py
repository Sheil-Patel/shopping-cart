# shopping_cart.py

#from pprint import pprint


import csv

csv_file_path = "data/products.csv" # a relative filepath

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    products = []
    p = {"id": int, "name": str, "department": str , "aisle": str, "price":float}
    for row in reader:
        p["id"] = row["id"]
        p["name"] = row["name"]
        p["department"] = row["department"]
        p["aisle"] = row["aisle"]
        p["price"] = row["price"]
        #p = {(row["id"], row["name"], row["department"], row["aisle"], row["price"])}
        products.append(p)

for p in products:
    print(p["id"])

