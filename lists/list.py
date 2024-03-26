#!/bin/python3


#Lists are data structure
#when you have a list, everything inside it is called item

#Lists have brackets []

movies = ["When Harry Met Sally", "The Hangover", "The Perts of Being a Wallflower", "The Exorcist"]
print(movies[1]) #return the second item
print(movies[0]) #returns the first item in the list
print(movies[1:3])
print(movies) #returns everything in the list
print(movies[1:]) #returns everything in the list
print(movies[:1]) #returns everything after the first item
print(movies[-1]) #returns the last item


print(len(movies)) #add the the list
movies.append('JAWS')
print(movies)

movies.pop() #remove from the list
print(movies)

movies.pop(0) #removes the first item
print(movies)

