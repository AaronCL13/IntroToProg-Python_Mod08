# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# ALanphear,3.3.21,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
        __init__(self, product_name="", product_price=0.0): initializes object with product name and product price
        product_name(self, product_name): sets product name
        product_price(self, product_price): sets product price
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALanphear,3.3.21,Modified code to complete assignment 8
    """

    # Constructor - Initializes each time an object is created
    def __init__(self, product_name="", product_price=0.0):
        self.__product_name = product_name  # private attribute
        self.__product_price = product_price  # private attribute

    @property  # Getter/Accessor
    def product_name(self):
        return self.__product_name

    @property  # Getter/Accessor
    def product_price(self):
        return self.__product_price

    @product_name.setter  # Setter/Mutator
    def product_name(self, product_name):
        if product_name == "":
            print("The product name cannot be blank.")
        elif str(product_name).isnumeric():
            print("The product name cannot be a number.")
        else:
            self.__product_name = product_name

    @product_price.setter  # Setter/Mutator
    def product_price(self, product_price):
        if str(product_price).isalpha():
            print("The product price cannot be a string.")
        else:
            self.__product_price = product_price


# p1 = Product("Wood", 10)
#
# print(p1.product_name, p1.product_price)
# p1.product_name = 15
# p1.product_price = "test"
# print(p1.product_name, p1.product_price)
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass
    # TODO: Add code to show menu to user
    # TODO: Add code to get user's choice
    # TODO: Add code to show the current data from the file to user
    # TODO: Add code to get product data from user
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

