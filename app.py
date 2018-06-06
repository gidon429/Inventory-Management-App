import csv
import os

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname("products_app"), "db", filename)
    products = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for ordered_dict in reader:
        #print(row["name"], row["price"])
            products.append(dict(ordered_dict))
    return products

products = read_products_from_file()
product_count = str(len(products))

print("-----------------------------------")
print("INVENTORY MANAGEMENT APPLICATION")
print("-----------------------------------")
print("Welcome @gidon429")
print("There are " + product_count + " products in the database.")
print("operation | description")
print("--------- | ------------------")
print("'List'    | Display a list of product identifiers and names.")
print("'Show'    | Show information about a product.")
print("'Create'  | Add a new product.")
print("'Update'  | Edit an existing product.")
print("'Destroy' | Delete an existing product.")
print("'Reset'   | Restore the original file")

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)


def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    products = read_products_from_file(from_filename)
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def find_product(product_id, all_products):
    matching_products = [p for p in all_products if int(p["id"]) == int(product_id)]
    matching_product = matching_products[0]
    return matching_product

def auto_incremented_product_id(products):
    if len(products) == 0:
        return 1
    else:
        product_ids = [int(p["id"]) for p in products]
        return max(product_ids) + 1

def editable_product_attributes():
    attribute_names = [attr_name for attr_name in ["id", "name", "aisle", "department", "price"] if attr_name != "id"]
    return attribute_names

def is_valid_price(my_price):
    try:
        float(my_price)
        return True
    except Exception as e:
        return False

def user_chosen_product(all_products):
    try:
        product_id = input("Please enter the product's identifier: ")
        product = find_product(product_id, all_products)
        return product
    except ValueError as e: return None
    except IndexError as e: return None


def delete_product(product, all_products):
    del all_products[all_products.index(product)]

def product_not_found():
    print("Could not find a product with that identifier")

def wrong_price_format():
    print(f"That format is not valid for product price, please enter an integer with two decimal places")

def run():
    products = read_products_from_file()

    function = input("Please select an operation:")

    if function == "List":
        print("-----------------------------------")
        print(f"LISTING {len(products)} PRODUCTS:")
        print("-----------------------------------")
        for p in products:
            print("#" + str(p["id"]) + ": " + p["name"])

    elif function == "Show":
        product_choice = user_chosen_product(products)
        if product_choice == None: product_not_found()
        else:
            print("-----------------------------------")
            print("SHOWING A PRODUCT:")
            print("-----------------------------------")
            print(product_choice)

    elif function == "Create":
        new_product = {}
        new_product["id"] = auto_incremented_product_id(products)
        for attribute_name in editable_product_attributes():
            new_val = input(f"Please input the product's '{attribute_name}': ")
            if attribute_name == "price" and is_valid_price(new_val) == False:
                wrong_price_format()
                return
                print("-----------------------------------")
                print("CREATING A NEW PRODUCT:")
                print("-----------------------------------")
                print(new_product)
            new_product[attribute_name] = new_val
        products.append(new_product)
        write_products_to_file(products=products)

    elif function == "Destroy":
        product = user_chosen_product(products)
        if product == None: product_not_found()
        else:
            print("-----------------------------------")
            print("DESTROYING A PRODUCT:")
            print("-----------------------------------")
            print(product)
            delete_product(product, products)
            write_products_to_file(products=products)

    elif function == "Update":
        existing_product = user_chosen_product(products)
        if existing_product == None: product_not_found()
        else:
            for attribute_name in editable_product_attributes():
                new_val = input(f"What is the product's new '{attribute_name}' (currently: '{existing_product[attribute_name]}')?")
                if attribute_name == "price" and is_valid_price(new_val) == False:
                    wrong_price_format()
                    return
                    print("-----------------------------------")
                    print("UPDATING A PRODUCT:")
                    print("-----------------------------------")
                    print(product)
                existing_product[attribute_name] = new_val
                write_products_to_file(products=products)

    elif function == "Reset":
        print("RESET TO DEFAULT")
        reset_products_file()

    else:
        print("Unrecognized operation, please try again.")

if __name__ == "__main__":
    run()
