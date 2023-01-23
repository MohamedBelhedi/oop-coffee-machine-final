from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    print("Welcome to the Coffee Machine choose your drink")
    menu.get_cost()
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "cost":
        menu.get_cost()
    if choice == options:
        print("geht weiter")
        continue
    elif choice not in options or choice == None:
        print("doenst exist try again")
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(
                drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
