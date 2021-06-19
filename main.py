from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
machine_off = False

while not machine_off:
    options = menu.get_items()
    customer_input = input(f"What would you like? ({options}):")
    if customer_input == "off":
        machine_off = True
    elif customer_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(customer_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


quit()