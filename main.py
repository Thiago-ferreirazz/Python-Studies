import os
import sys

# Menu of coffee drinks with ingredients and costs
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initial resources available
resources = {
    "water": 500,
    "milk": 300,
    "coffee": 250,
}

# Initial profit
profit = 0

def clear():
    """Clears the console."""
    return os.system('cls' if os.name == 'nt' else 'clear')

def number_checker(string):
    """Prompts user for a number and ensures valid input."""
    number = input(string)
    while not number.isnumeric():
        number = input("Type a valid number: ")
    return int(number)

def select_coffee(string):
    """Prompts user to select a coffee drink and ensures valid input."""
    coffee = input(string).lower()
    while coffee not in ["latte", "espresso", "cappuccino", "off", "report"]:
        coffee = input("Please enter a valid term: ").lower()
    return coffee

def check_resources(ingredients):
    """Checks if there are enough resources to make the selected coffee."""
    for key in ingredients:
        if resources[key] < ingredients[key]:
            print(f"Sorry, there is not enough {key}.")
            return False
    return True

def process_payment():
    """Processes the payment from the user and returns the total amount of money inserted."""
    print("Please insert coins.")
    total = number_checker("How many quarters? ") * 0.25
    total += number_checker("How many dimes? ") * 0.1
    total += number_checker("How many nickels? ") * 0.05
    total += number_checker("How many pennies? ") * 0.01
    return total

def is_payment_successful(money_received, drink_cost):
    """Checks if the payment is sufficient and processes the transaction."""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, ingredients):
    """Deducts the required ingredients from the resources and serves the coffee."""
    for key in ingredients:
        resources[key] -= ingredients[key]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# Main loop to run the coffee machine
while True:
    print(f"Menu:\n\nLatte: ${menu['latte']['cost']}\nCappuccino: ${menu['cappuccino']['cost']}\nEspresso: ${menu['espresso']['cost']}")
    choice = select_coffee("\nPlease select your drink: ")
    if choice == "report":
        # Display remaining resources and profit
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        sys.exit()
    elif choice == "off":
        # Shut down the machine
        print("Shutting down...")
        sys.exit()
    else:
        drink = menu[choice]
        if check_resources(drink["ingredients"]):
            payment = process_payment()
            if is_payment_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        input("\nPress any key to place another order: ")
        clear()
