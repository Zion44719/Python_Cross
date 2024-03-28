#!/bin/python3

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

print(my_dict["key2"])

#You can also change the value associated with a key or add new key-value pairs:

my_dict["key1"] = "new_value"
my_dict["key4"] = "value changed"

print(my_dict["key4"])

drinks = {"white Russian": 7, "Old Fashion": 10, "Lemon Drop": 8} #Drink is the key while price is the value
print(drinks)

drinks["White Russian"] = 8
print(drinks)

print(drinks.get("White Russian"))

#####
employees = {'Finance': ['Bob', "Linda", "Tine"], "IT": ["Gene", "Louise", "Teedy"], "HR": ["Jimmy Jr", "Mort"]}

print(employees)

#To add key and value
employees["Legal"] = ["Mr. Frond"]
print(employees)


employees.update({"sales": ["Andie", "Ollie"]})
print(employees)


help()
print(help)



