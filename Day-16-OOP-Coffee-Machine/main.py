from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = Menu()
coffee_maker= CoffeeMaker()
money= MoneyMachine()

machine=True
while machine:
    order= input(f"What would you like? ({menu_item.get_items()}) :")
    if order == "off":
        machine= False
    elif order == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = menu_item.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)