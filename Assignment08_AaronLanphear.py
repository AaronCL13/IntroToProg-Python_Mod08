# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# ALanphear,3.3.21,Modified code to complete assignment 8 - Product Class
# ALanphear,3.4.21,Modified code to complete assignment 8 - Processing Class
# ALanphear,3.5.21,Modified code to complete assignment 8 - IO Class/Main Body
# ALanphear,3.6.21,Modified code to complete assignment 8 - Main Body/Error Handling
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
        with open(file_name, "r") as f:
            for row in f:
                product, price = row.split(",")
                row = {"Product": product.strip(), "Price": price.strip()}
                list_of_rows.append(row)
            return list_of_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """ Saves data from a list to a file

        :param file_name: (string) name of file
        :param list_of_rows: (list) you want saved to file
        :return: string message

        """
        with open(file_name, "w") as f:
            table = ""
            for row in list_of_rows:
                new_row = row["Product"] + "," + str(row["Price"]) + "\n"
                table += new_row
            f.write(table)
            return "Current list saved to your file!"
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
        1) Display Current Product List
        2) Add Product to List
        3) Save Product List to File and Exit Program
        """)

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string

        """
        user_choice = str(input("What choice would you like to make? [1, 2, or 3] - ")).strip()
        print()  # extra line for looks
        return user_choice

    @staticmethod
    def print_current_products_in_list(list_of_rows):
        """ Shows the current products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing

        """
        print("******* The Current Products in Your List are: *******")
        for row in list_of_rows:
            print("Product: " + row["Product"] + ' --- ' + "Price: " + str("$%.2f" % float((row["Price"]))))
        print("******************************************************")
        # print()  # Add an extra line for looks

    @staticmethod
    def input_new_product_and_price():
        """ Accepts user input for new product and price

        :return: product and price

        """
        product = input("What product would you like to add? - ")
        price = float(input("What is the product's price? - "))
        return product, price
# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
def main():
    # Load data from file into a list of product objects when script starts
    try:
        FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
    except FileNotFoundError:  # Display this error if the file has not been created yet
        print()
        print("...There was no file to load data from...")
        print("...Enter products so a file can be saved...")
    choice = ""
    while choice != "3":
        # Show user a menu of options
        IO.print_menu_tasks()
        # Get user's menu option choice
        choice = IO.input_menu_choice()
        # Show user current data in the list of product objects
        if choice == "1" and lstOfProductObjects == []:
            print("...There is no current list to display...")
            print("...You must first add a product to your list...")
        elif choice == "1":
            IO.print_current_products_in_list(lstOfProductObjects)
        # Let user add data to the list of product objects
        elif choice == "2":
            try:
                new_product_name, new_product_price = IO.input_new_product_and_price()
                if new_product_name.isnumeric():
                    print("\n...The product name cannot be a number...")
                    print("...Please make your choice again...")
                    continue
            except ValueError:
                print("\n...The price must be a valid number...")
                print("...Please make your choice again...")
            else:
                new_product = Product(new_product_name, new_product_price)
                status = new_product.add_to_list(lstOfProductObjects)[1]
                print(status)
        # let user save current data to file and exit program
        elif choice == "3":
            status = FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print(status, "Goodbye!")
        else:
            print("'" + choice + "' " + "is not a valid option! Please try again.")


# Run the program
main()
input("\nPress [Enter] to Exit.")
# Main Body of Script  ---------------------------------------------------- #