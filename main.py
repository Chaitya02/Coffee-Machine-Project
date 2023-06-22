MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


money = 0.0


def process(selected):
    """ Checks for required resources """
    global resources
    chosen = MENU[selected]
    water_req = chosen["ingredients"]["water"]
    milk_req = chosen["ingredients"]["milk"]
    coffee_req = chosen["ingredients"]["coffee"]

    if water_req > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    if milk_req > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if coffee_req > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


def coins():
    """ Calculates the total value inserted """
    print("Please insert coins.")
    quarters = int(input("how much quarters? - "))
    dimes = int(input("how much dimes? - "))
    nickles = int(input("how much nickles? - "))
    pennies = int(input("how much pennies? - "))
    total_coins = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return total_coins


def make_coffee(drink_name):
    """ Coffee is being made """
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def espresso():
    """ Adding the money and reducing the resources """
    global money, resources
    if process("espresso"):
        total = coins()
        cost = MENU["espresso"]["cost"]
        if total > cost:
            money += cost
            change = total - cost
            print(f"Here is ${round(change, 2)} dollars in change.")
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["milk"] -= MENU["espresso"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            make_coffee("espresso")
        else:
            print("Sorry that's not enough money. Money refunded.")


def latte():
    """ Adding the money and reducing the resources """
    global money, resources
    if process("latte"):
        total = coins()
        cost = MENU["latte"]["cost"]
        if total > cost:
            money += cost
            change = total - cost
            print(f"Here is ${round(change, 2)} dollars in change.")
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            make_coffee("latte")
        else:
            print("Sorry that's not enough money. Money refunded.")


def cappuccino():
    """ Adding the money and reducing the resources """
    global money, resources
    if process("cappuccino"):
        total = coins()
        cost = MENU["cappuccino"]["cost"]
        if total > cost:
            money += cost
            change = total - cost
            print(f"Here is ${round(change, 2)} dollars in change.")
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            make_coffee("cappuccino")
        else:
            print("Sorry that's not enough money. Money refunded.")


def report(resources):
    """ Print the current resources of the machine """
    global money
    for key in resources:
        if key == "coffee":
            print(f"{key}: {resources[key]}g")
        else:
            print(f"{key}: {resources[key]}ml")
    print(f"money: ${money}")


def machine():
    """ Main Coffee Machine """
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "espresso":
        espresso()
        machine()
    elif request == "latte":
        latte()
        machine()
    elif request == "cappuccino":
        cappuccino()
        machine()
    elif request == "report":
        report(resources)
        machine()
    elif request == "off":
        return
    else:
        print("Wrong request! Try again")
        machine()


machine()
