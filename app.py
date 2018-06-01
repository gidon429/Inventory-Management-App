import csv
import os


#print("-----------------------------------")
#print("INVENTORY MANAGEMENT APPLICATION")
#print("-----------------------------------")
#print("Welcome {username}")
#print("There are {products_count} products in the database.")
#print("operation | description")
#print("--------- | ------------------")
#print("'List'    | Display a list of product identifiers and names.")
#print("'Show'    | Show information about a product.")
#print("'Create'  | Add a new product.")
#print("'Update'  | Edit an existing product.")
#print("'Destroy' | Delete an existing product.")

def menu(username="@gidon429", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu


import csv

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname("products_app"), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []

    #TODO: open the file and populate the products list with product dictionaries
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
        #print(row["name"], row["price"])
            products.append(dict(row))

    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() # uses fieldnames set above
        for product in products:
            writer.writerow(product)
    #TODO: open the file and write a list of dictionaries. each dict should represent a product.

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    #print(products)
    write_products_to_file(filename, products)

def run():
    # First, read products from file...
    products = read_products_from_file()

operations = []

    # Then, prompt the user to select an operation...
while True:
    operation = input("Please select an operation:")
    if operation == "DONE":
        break
    else:
        operations.append(float(operation))

    print(menu(username="@gidon429")) #TODO instead of printing, capture user input

    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    #TODO: handle selected operation

    # Finally, save products to file so they persist after script is done...
    write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
