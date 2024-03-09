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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


COINS = {
    "Quarters" : 0.25,
    "Dimes" : 0.10,
    "Nickles" : 0.05,
    "Pennies" : 0.01,
}

money = 0


# report printing
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# processing coins
def insert_coins(coffee):
    amount_paid = 0
    print("Please insert coins.")
    for key in COINS:
        number_of_coins = int(input(f"{key}(${COINS[key]}): "))
        total_amount = number_of_coins * COINS[key]
        amount_paid += total_amount
        # finish early if more than enough
        if amount_paid >= MENU[coffee]['cost']:
            break
    print(f"You have inserted ${amount_paid}")
    return amount_paid


# making sure amount is sufficient for coffee
def  check_payment(user_amount, coffee_price):
    if user_amount < coffee_price:
        return False
    else:
        global money
        change = user_amount - coffee_price
        print(f"Here is your ${round(change, 2)} in change.")
        money  += coffee_price
        return True


# checking sufficient resources
def resource_checker(coffee):
    for key in resources:
        if key not in MENU[coffee]["ingredients"]:
            resources[key] - 0
        elif resources[key] < MENU[coffee]["ingredients"][key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True    
            

# refilling the tank
def refil():
    for key in resources:
        refil_amount = int(input(f"Insert amount to refill for {key}:"))
        resources[key] += refil_amount

# asking user what they like
#  adding a turn off prompt to end loop
finish = False
while not finish:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        print(f"A {user_choice} cost ${MENU[user_choice]['cost']}.")
        ingredients_enough = resource_checker(user_choice)
        # Making Coffee
        if ingredients_enough == True:
            paid = check_payment(insert_coins(user_choice),  MENU[user_choice]['cost'])
            if paid == True:
                for key in resources:
                    if key not in MENU[user_choice]["ingredients"]:
                        resources[key] - 0
                    else:
                        resources[key] -= MENU[user_choice]["ingredients"][key]
            else:
                print("Sorry, that's not enough. Your money will be refunded.")
        else:
            print("We will serve you next time!")
    # Turning machine off
    elif user_choice == "off":
        print("Turning off the coffee machine.")
        finish = True
    # add report function
    elif user_choice == "report":
        report()
    elif  user_choice == "refill":
        refil()
    else:
        print("Invalid selection. Try Again")


# refill