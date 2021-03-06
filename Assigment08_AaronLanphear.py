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

        add_to_list(self, list_of_rows): adds product to list provided -> list of products

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

    def add_to_list(self, list_of_rows):
        row = {"Product": self.__product_name, "Price": self.__product_price}
        list_of_rows.append(row)
        return list_of_rows, "\nThe product has been added to your list!"

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
        save_data_to_file(file_name, list_of_product_objects): saves list to a file

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALanphear,3.4.21,Modified code to complete assignment 8

    """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows

        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for row in file:
            product, price = row.split(",")
            row = {"Product": product.strip(), "Price": str("%.2f" % float(price.strip()))}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """ Saves data from a list to a file

        :param file_name: (string) name of file
        :param list_of_rows: (list) you want saved to file
        :return: string message

        """
        file = open(file_name, "w")
        table = ""
        for row in list_of_rows:
            new_row = row["Product"] + "," + str(row["Price"]) + "\n"
            table += new_row
        file.write(table)
        file.close()
        return "\nCurrent list saved to your file!"


# lstOfProductObjects = [{'Product': 'Wood', 'Price': 10}]
# print(lstOfProductObjects)
# p1 = Product("Nails", 5)
# p1.add_to_list(lstOfProductObjects)
# print(lstOfProductObjects)
# FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
# data = FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
# print(data)
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs input/output functions

    methods:
        print_menu_tasks(): display choice menu to user

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        ALanphear,3.5.21,Created Class

    """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing

        """
        print("""
        Choice Menu
        1) Display Current Data
        2) Add Data to List
        3) Save Data to File and Exit Program
        """)
        # print()  # extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string

        """
        choice = str(input("What choice would you like to make? [1, 2, or 3] - ")).strip()
        # print()  # extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user

    @staticmethod
    def print_current_products_in_list(list_of_rows):
        """ Shows the current products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing

        """
        print("******* The current Products in Your List are: *******")
        for row in list_of_rows:
            print("Product: " + row["Product"] + ' --- ' + "Price: " + str("%.2f" % (row["Price"])))
        print("******************************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user

    @staticmethod
    def input_new_product_and_price():
        """ Accepts user input for new product and price

        :return: product_name and product_price

        """
        product_name = input("What product would you like to add? - ")
        product_price = input("What is the product's price? - ")
        return product_name, product_price

# IO.print_menu_tasks()
# IO.input_menu_choice()
# IO.print_current_products_in_list(lstOfProductObjects)
# new_product, new_price = IO.input_new_product_and_price()
# print(new_product, new_price)


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

