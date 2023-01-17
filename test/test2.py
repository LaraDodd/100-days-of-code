import pandas


# ========The beginning of the class==========
class Shoe:
    """Creates show object with various stock data

    Attributes:
        country - where it is
        code -
        product -
        cost -
        quanitity -

    Methods:
        get_cost - returns cost of shoe
        get_quantity - returns quantity of shoes
        __str__ - returns string of class"""

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        output = f"Country: {self.country}\n"
        output += f"Product code: {self.code}\n"
        output += f"Product: {self.product}\n"
        output += f"Product cost: {self.cost}\n"
        output += f"Product quantity: {self.quantity}\n"
        return output


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# =============Functions outside the class==============
def read_shoes_data():
    """This function will open the file inventory.csv in a pd dataframe
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list."""
    shoes_df = pandas.read_csv("inventory.csv")
    shoes_dict = shoes_df.to_dict(orient="records")
    for data in shoes_dict:
        shoe_object = Shoe(data["Country"], data["Code"], data["Product"], data["Cost"], data["Quantity"])
        shoe_list.append(shoe_object)
    return shoes_dict


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list. Also adds shoe data to csv.
    '''
    country = input("Please enter the country that the shoes are in: ")
    code = input("Please enter the product code: ")
    product = input("Please enter the name of the shoe: ")
    cost = int(input("Please enter the cost of the shoe: "))
    quantity = int(input("Please enter the stock quantity: "))

    data_dict_item = {'Country': country,
                      'Code': code,
                      'Product': product,
                      'Cost': cost,
                      'Quantity': quantity,
                      }

    shoes_dict_list = read_shoes_data()
    shoes_dict_list.append(data_dict_item)

    df = pandas.DataFrame(shoes_dict_list)
    df.to_csv("inventory.csv", index=False)

    shoe_object = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_object)
    return


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    # read_shoes_data()
    # for shoe in shoe_list:
    #     print(shoe.__str__())

    # leaving above for marker but using pd df as cleaner:
    shoes_dict_list = read_shoes_data()

    df = pandas.DataFrame(shoes_dict_list)
    print(df)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    shoes_df = pandas.read_csv("inventory.csv")
    min_qty_product = shoes_df[shoes_df.Quantity == shoes_df.Quantity.min()]
    print(f"The product/s with the lowest stock is/are:\n{min_qty_product}\n")

    try:
        quantity = int(input("Enter the number that you would like to restock product by "))
    except TypeError:
        print("This is not a number")
        re_stock()
    else:
        new_quantity = shoes_df.Quantity.min()+quantity
    finally:
        index = shoes_df.index[shoes_df.Quantity == shoes_df.Quantity.min()]
        shoes_df.loc[index, "Quantity"] = new_quantity

    #write to csv
    shoes_df.to_csv("inventory.csv", index=False)

    print(f"The new quantity of {min_qty_product.Product.to_string(index=False)} is {new_quantity}")



def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''


def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# shoe = Shoe("UK", "2", "3", "4", "5")
# print(type(shoe))
# print(shoe.product)
#
# shoes = read_shoes_data()
#
# for shoe in shoes:
#     print(shoe.product)


view_all()
print()
re_stock()
