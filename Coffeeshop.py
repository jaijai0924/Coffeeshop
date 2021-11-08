# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import math
from decimal import Decimal
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


def inserted_coin(inserted_quarters, inserted_dimes,inserted_nickles,
                  inserted_pennies):
    #returns total 
    inserted_coins = Decimal(inserted_quarters)+Decimal(inserted_dimes)
    +Decimal(inserted_nickles)+Decimal(inserted_pennies)
    format_coins = "{:.2f}".format(inserted_coins)
    math_coins = inserted_quarters+inserted_dimes+inserted_nickles+inserted_pennies
    return inserted_coins
    print("Current Balance :",format_coins)


def is_transaction_sucessful(money_received, drink_cost):
    """return true when payment is accepte, or false is insuf"""
    if money_received>= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.")
        return False
    
def resource_check(order_ingredients):
    for i in order_ingredients:
       if order_ingredients[i] >= resources[i]:
           print(f"Sorry not enough{i}")
           return False
       return True

def make_coffee(drink_name, order_ingredients):
    """dedcut """       
    for i in order_ingredients:
           resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name} ☕️")

print("Getting started: Insert coins")
print("How many? ")
inserted_quarters = int(input("Enter quarters: "))
inserted_quarters = inserted_quarters*.25
print("How many?")
inserted_dimes = int(input("Enter dimes: "))
inserted_dimes = inserted_dimes*.10
print("How many?")
inserted_nickles = int(input("Enter nickles: "))
inserted_nickles =  inserted_nickles*.05
print("How many?")
inserted_pennies = int(input("Enter pennies: "))
inserted_pennies = inserted_pennies*.01

balance = inserted_quarters+ inserted_dimes+ inserted_nickles+inserted_pennies
#print(balance)
while True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
    current_resource = resources
    if coffee_choice == "espresso":
        drink = MENU[coffee_choice]
        if resource_check(drink["ingredients"]):
            payment =  balance
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(coffee_choice,drink["ingredients"])
            
            
    elif coffee_choice == "latte":
        drink = MENU[coffee_choice]
        resource_check(drink["ingredients"])
        if resource_check(drink["ingredients"]):
            payment =  balance
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(coffee_choice,drink["ingredients"])
    elif coffee_choice == "cappuccino":
        drink = MENU[coffee_choice]
        resource_check(drink["ingredients"])
        if resource_check(drink["ingredients"]):
            payment =  balance
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(coffee_choice,drink["ingredients"])
    elif coffee_choice == "report":
        format_coins = "{:.2f}".format(balance)
        # for key, value in resources.items():
        #     print(key,":",value)
        print(f"Water: {resources['water']}ml")
        print(f"Milk:  {resources['milk']}ml")
        print(f"Coffee:  {resources['coffee']}g")
        print("Current Balance :",format_coins)
    elif coffee_choice == "off":
        print("turning off...")
        break
    else:
        print("Not a choice, try again...")
    
    def check_resources():
        print("Current available resource: ", resources)
        


#def espresso():
 #   return 0