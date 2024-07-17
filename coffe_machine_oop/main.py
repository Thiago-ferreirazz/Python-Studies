import coffee_maker
import menu
import money_machine

menu = menu.Menu()
money_machine = money_machine.MoneyMachine()
coffee_maker = coffee_maker.CoffeeMaker()
options = menu.get_items()

while True:
    choice = input(f"What would you like to drink? {options}: ")
    while choice not in ["latte", "espresso", "cappuccino", "report", "off"]:
        choice = input(f"Type a valid option ({options}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        break
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
