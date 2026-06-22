MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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
money=0
owner_money=0
def check_resource (item,raw):
    if resources[raw] < MENU[item]["ingredients"][raw]:
        print(f"Sorry there is not enough {raw}.")

def left_resource(item):
    if resources["water"] >= MENU[item]["ingredients"]["water"] and resources["coffee"] >= MENU[item]["ingredients"]["coffee"] and resources["milk"] >= MENU[item]["ingredients"]["milk"]:
        global money
        print("Insert the coins! ")
        money+=int(input("How many quarters? "))* 0.01
        money+=int(input("How many dimes? ")) * 0.05
        money+=int(input("How many nickles? ")) * 0.10
        money+=int(input("How many pennis? ")) * 0.25

        if money>=MENU[item]["cost"]:
            global owner_money
            owner_money+=MENU[item]["cost"]
            refund=money-MENU[item]["cost"]
            resources["water"]-=MENU[item]["ingredients"]["water"]
            resources["coffee"]-=MENU[item]["ingredients"]["coffee"]
            resources["milk"]-=MENU[item]["ingredients"]["milk"]
            print(f"Here is ${refund} in change.")
            print(f"Here is your {item}. Enjoy!")

        else:
            print("Sorry that's not enough money. Money refunded.")
            money=0
    else :
        # for i in item:
        #     if item[i]>=resources[i]:
        #         print(f"Sorry there is not enough {i}.")

        check_resource(item,"water")
        check_resource(item,"coffee")
        check_resource(item,"milk")


machine=True
while machine==True:
    demand=input("What would you like? (espresso/latte/cappuccino): ")
    if demand== "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: ${owner_money}")
    elif demand=="off":
        machine=False
    else:
        left_resource(demand)