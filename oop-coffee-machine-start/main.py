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
        money_machine.report
    else:
        print("test")
        is_on = False

