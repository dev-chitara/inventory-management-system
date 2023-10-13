import csv
from rich.console import Console
from rich.table import Table

from schemas.products import  get_products, create_products, get_product, update_product, delete_product
from schemas.suppliers import get_suppliers, create_suppliers, get_supplier, update_supplier, delete_supplier
from schemas.inventory import get_inventory_list, create_inventory, get_inventory, update_inventory, delete_inventory

# Products Test
# create_products(Product,"Apple", "Apple is very delicious", 20, 4)
# create_products(Product,"Mango", "Mango is very delicious", 25, 2)
# create_products(Product,"Banana", "Banana is very delicious", 30, 4)
# create_products(Product,"Grapes", "Grapes is very delicious", 40, 20)
# create_products(Product,"Watermelon", "Watermelon is very delicious", 35, 1)
# create_products("Strawberry", "Strawberry is very delicious", 30, 10)

# print(get_products())

# print(get_product("eb5c8796-614b-4557-a7db-9f284396322a"))

# update_product("eb5c8796-614b-4557-a7db-9f284396322a","Green apple", "Apple is very delicious", 20, 4)

# print(delete_product("fc555d42-f712-41f8-befc-713f64b41568"))


# Supplier Test
# create_suppliers("Dev", 1234567891)
# create_suppliers("Rahul", 9624647517)
# create_suppliers("Ram", 3768642873)
# create_suppliers("Kuldeep", 3674616844)
# create_suppliers("Mohit", 9375272562)
# create_suppliers("Harshit", 7142897832)

# print(get_suppliers())

# print(get_supplier("06c4bbf1-9c0e-42a1-a462-90c7583b1d6f"))

# print(update_supplier("2c604345-290d-45a4-bac9-480fe60b1a39", "Piyush", 8537321868))

# print(delete_supplier("a364a28b-7a7f-4fc2-87bf-f34897c53e8a"))


COLUMN_NAMES = ["Serial No.", "Name", "Location", "Type"]
table = Table(title = "Inventory Name List")

for item in COLUMN_NAMES:
    table.add_column(item)

with open("./db/inventory.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for num, row in enumerate(reader, 1):
        table.add_row(
            str(num), 
            row.get("name"), 
            row.get("location"), 
            row.get("inventory_type")
        )

    console = Console()
    console.log(table)


COLUMNS = ["Serial No.", "Option"]
ROWS = ["Inventory", "Product", "Supplier"]
option_table = Table()

for item in COLUMNS:
    option_table.add_column(item)

for num, option in enumerate(ROWS, 1):
    option_table.add_row(str(num), option)

console = Console()
console.log(option_table)

def get_products_table():
    COLUMNS = ["Id", "Name", "Descrption", "Price", "Quantity"]    
    table = Table()

    for item in COLUMNS:
        table.add_column(item)

    for item in get_products():
        table.add_row(item["id"], item["name"], item["description"], item["price"], item["quantity"])

    console = Console()
    console.log(table)


def inventory_table():
    COLUMNS = ["Serial No.", "Option"]
    table = Table()
    ROWS = ["get_products", "create_products", "get_product", "update_product", "delete_product"]

    for item in COLUMNS:
        table.add_column(item)

    for num, option in enumerate(ROWS, 1):
        table.add_row(str(num), option)

    console = Console()
    console.log(table)
    
    user_input = input("Enter a serial number from above table:")

    match user_input:
        case "1":
            get_products_table()

        case "2":
            product_name = input("Enter Product Name :")
            product_description = input("Enter Product Description :")
            product_price = input("Enter Product Price :")
            product_quantity = input("Enter Product Quantity :")
            create_products(product_name, product_description, product_price, product_quantity)
            get_products_table()
        
        case "3":
            product_id = input("Enter Product Id :")
            COLUMNS = ["Id", "Name", "Descrption", "Price", "Quantity"]    
            table = Table()

            for item in COLUMNS:
                table.add_column(item)

            item = get_product(product_id)
            table.add_row(item["id"], item["name"], item["description"], item["price"], item["quantity"])
            console = Console()
            console.log(table)

        case "4":
            product_id = input("Enter Product Id :")
            product_name = input("Enter Product Name :")
            product_description = input("Enter Product Description :")
            product_price = input("Enter Product Price :")
            product_quantity = input("Enter Product Quantity :")           
            update_product(product_id, product_name, product_description, product_price, product_quantity)
            get_products_table()

        case "5":
            product_id = input("Enter Product Id :")
            delete_product(product_id)
            get_products_table()
            
        case _:
            print("Invalid Serial No.")



user_input = input("Enter a serial number from above table:")

match user_input:
    case "1":
        pass

    case "2":
        inventory_table()

    case _:
        print("Invalid Serial No.")
