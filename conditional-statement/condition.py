#!/bin/python3

#Conditional Statement
#

def nl():
    print('\n')
nl()

def drink(money):
    if money >= 2:
        return "Buy bread!"
    else: 
        return "Your money can't buy bread!"
print(drink(3))
print(drink(1))


def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, Kid!"
    else:
        return "You dont have enough money and you're too young"
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))
