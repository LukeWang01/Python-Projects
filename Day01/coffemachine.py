MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f" Not enough {item}")
            return False
    return True


def process_coins():
    """Return the money inserted"""
    print("Please insert coins")
    total = int(input("How many quarters? : ")) * 0.25
    return total


def is_transaction_ok(payment_rec, drink_cost):
    if payment_rec >= drink_cost:
        change = round(payment_rec - drink_cost, 2)
        global profit
        profit += drink_cost
        return True
    else:
        print("Money is not enough")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f" Here is your {drink_name}  ☕️   ")


is_on = True


while is_on:
    choice = input("what coffee would you like?")
    if choice == "off":
        choice = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_ok(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

