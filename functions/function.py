#!/bin/python3

#Organized block of code

def who_am_i():
    name = "Oluwafemi"
    age = 30
    print("My name is " + name + " and i am " + str(age) + " years old.")
who_am_i()

#Adding Parameter
def add_one_hundred(num):
    print(num + 100)
add_one_hundred(100)


#Multiple Parameters
def add(x,y):
    print(x + y)
add(7, 7)

def multiply(x,y):
    return x * y
print(multiply(7, 7))


def square_root(x):
    print(x ** .5)
square_root(64)

 #Print New Line
 #print('\n')
 
def new_line():
     print('\n')
new_line()