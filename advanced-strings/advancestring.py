#!/bin/python3

my_name = "Oluwafemi"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4])
print(sentence.split())


#Join a sentence
sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)


#To add quote in a string or character escaping
quote = "He said, \"give me all your money\""
print(quote)

#To add quote, you can use single quote
quotes = "He said, 'give me all your money'"
print(quotes)


#String Formatting
name = "Alice"
age = 30
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)
# Output: Name: Alice, Age: 30

f_string = f"Name: {name}, Age: {age}"
print(f_string)
# Output: Name: Alice, Age: 30

#Regular Expressions: Python's re module allows you to work with regular expressions, which are powerful tools for pattern matching and string manipulation.
import re

text = "The quick brown fox jumps over the lazy dog"
pattern = r"\b\w{5}\b"
matches = re.findall(pattern, text)
print(matches)
# Output: ['quick', 'brown', 'jumps']


#String Concatenation: You can concatenate strings using the + operator or the join method.

str1 = "Hello"
str2 = "World"
concatenated_string = str1 + " " + str2
print(concatenated_string)
# Output: "Hello World"


#String Methods: Python provides many built-in methods for working with strings, such as split, join, replace, strip, startswith, endswith, lower, upper, and more

text = "   Hello, World!   "
print(text.strip())  # Output: "Hello, World!"

too_much_space = "        Hello World       "
print(too_much_space.strip())

print("A" in "Apple")
print("a" in "Apple")

#Trying to find a specific word or letter
letter = "A"
word = "Apple"
print(letter.lower() in word.lower())