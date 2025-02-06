#Dictionary with details about the ingredients and cost of Coffees
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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

def refill():
    global resources
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

#This variable will check if the machine is switched on or off
machine_status = True

while machine_status:
    user_input = input("What would you like?[cappuccino / latte / espresso]: ")

    #The user can use report to check resources left, refill to refill the resources and off to switch off the machine
    if user_input == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nProfit: {profit}")
    elif user_input == "refill":
        refill()
        print("Machine has been refilled successfully.")
    elif user_input == "off":
        print("Machine turning off....")
        break

    if user_input in MENU:    
        enough_resources = True
        
        #This for-loop checks if the machine has ample resources for the desired product
        for ingredient in MENU[user_input]["ingredients"]:
            if resources[ingredient] < MENU[user_input]["ingredients"][ingredient]:
                print("Sorry...Not enough resources available")
                enough_resources = False
                break
        
        if enough_resources == False:
            break
        
        #Here we deduct the resources needed to make the coffee
        for deduct in MENU[user_input]["ingredients"]:
            resources[deduct] = resources[deduct] - MENU[user_input]["ingredients"][deduct]
        
        drink_cost = MENU[user_input]["cost"]
        print(f"Please pay {drink_cost}$")

        while True:
            try:
                user_penny = int(input("How many pennies [0.01$]"))*0.01
                user_nickel =int(input("How many nickels [0.05$]"))*0.05
                user_dime = int(input("How many dimes [0.10$]"))*0.10
                user_quarter = int(input("How many quarters [0.25$]"))*0.25
                break
            except ValueError:
                print("Please enter Number of coins(eg, 1, 2, 3, 4)")

        user_total = user_penny + user_nickel + user_dime + user_quarter

        if user_total >= drink_cost:
            if user_total > drink_cost:
                print(f"Here's your change: {user_total - drink_cost}$\n")
            print("Here's your order.\nThanks for using Benny Beans Coffee.")
            profit += drink_cost
        else:
            print("Not enough money. Money refunded...")
            break