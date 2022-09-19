# Arrays python

number_array = [0,1,2,3,4,5,6,7,8,9,10]
print (type,number_array)

string_array = ["Father", "Hanka", "Marosko", "Mother"]
combined_array = [1, "Hanka", True, 2.0]
print (string_array)
print (combined_array)

cars = ["Ford", "Volvo", "BMW"]
print (cars[0])

# Use the len() method to return the length of an array
length = len(cars)
print(length)  # print the number of elements in an array

# for in loop to loop through all the elements of an array
for x in cars:
    print (x)

# You can use the append() method to add an element to an array
cars.append ("Skoda")
print (cars)

# You can also use the pop() method to remove an element from the array
# You can also use the remove() method to remove an element from the array
cars.pop (3)
print (cars)
cars.remove ("BMW")
print (cars)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list ( or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
