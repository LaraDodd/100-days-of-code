from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()



print("Welcome to the coffee machine")
order = input(f"What would you like? {menu.get_items()}? ")

is_on = True


while is_on:
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(menu_item):

            print(f"That will cost ${menu_item.cost}")
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
                coffee_maker.report()
        is_on = False

