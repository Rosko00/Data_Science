# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data,
# the other 3 are List, Set, and Dictionary, all with different qualities and usage.

this_is_tuple_1 = ("apple", "banana", "cherry")
print (this_is_tuple_1)

# Tuple items are ordered, unchangeable, and allow duplicate values.
# When we say that tuples are ordered, it means that the items have a defined order,
# and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, 
# add or remove items after the tuple has been created.
# Since tuples are indexed, they can have items with the same value

this_is_tuple_2 = ("apple", "banana", "cherry", "banana", "cherry", "apple")
print (this_is_tuple_2)

# Print the number of items in the tuple

this_is_tuple_2 = ("apple", "banana", "cherry", "banana", "cherry", "apple")
print(len(this_is_tuple_2))

# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.

this_is_tuple_3 = ("Marian",)
print (type(this_is_tuple_3))
# not a tuple
this_is_tuple_4 = ("Marian")
print (type(this_is_tuple_4))

# String, int and boolean data types
this_is_tuple_5 = ("apple", "banana", "cherry", 3, 5, 39, 41, True, False, False, True)
print (this_is_tuple_5)
print (type(this_is_tuple_5))

# You can access tuple items by referring to the index number, inside square brackets
this_is_tuple_6 = ("Marian", "Hanka", "Marosko")
print (this_is_tuple_6[1])  # Print the second item in the tuple:
print (this_is_tuple_6[-1])  # Negative indexing means start from the end.

this_is_tuple_7 = ("Marian", "Hanka", "Marosko", "Ferko", "Anicka", "Eva", "Martina")
print (this_is_tuple_7[2:5]) # Return the third, fourth, and fifth item
print (this_is_tuple_7[:4]) # This example returns the items from the beginning to, but NOT included, "Anicka": 
print(this_is_tuple_7[2:]) # This example returns the items from "Marosko" and to the end
print(this_is_tuple_7[-4:-1]) # This example returns the items from index -4 (included) to index -1 (excluded)

# To determine if a specified item is present in a tuple use the in keyword:
this_is_tuple_8 = ("Marian", "Hanka", "Marosko", "Ferko", "Anicka", "Eva", "Martina")
if "Hanka" in this_is_tuple_8:
    print ("Yes 'apple' is in the name tiple")

# Example
# But there is a workaround. You can convert the tuple into a list, 
# change the list, and convert the list back into a tuple
names_x_1 = ("Marian", "Hanka", "Marosko", "Ferko", "Anicka", "Eva", "Martina")
names_y_1 = list (names_x_1)
names_y_1[1] = "Hana"
names_x_1 = tuple(names_y_1)
print (names_x_1)

# add items (.append)
names_x_2 = ("Marian", "Hanka", "Marosko", "Ferko", "Anicka", "Eva", "Martina")
names_y_2 = list (names_x_2)
names_y_2 . append ("Marcel")
names_x_2 = tuple(names_y_2)
print (names_x_2)

names_x_3 = ("Marian", "Hanka", "Marosko", "Ferko", "Anicka", "Eva", "Martina")
names_y_3 = ("Marcelko", )
names_x_3 += names_y_3
print (names_x_3)

# Convert the tuple into a list, remove "Ferko", and convert it back into a tuple
names_x_4 = ("Marian", "Hanka", "Marosko", "Ferko", "Anicka", "Eva", "Martina")
names_y_4 = list (names_x_4)
names_y_4 . remove ("Ferko")
names_x_4 = tuple (names_y_4)
print (names_x_4)

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
# If the number of variables is less than the number of values, you can add an * to 
# the variable name and the values ​​will be assigned to the variable as a list
names_x_5 = ("Marian", "Marosko", "Anicka", "Eva", "Martina", "Hanka")
(man, boy, *woman,) = names_x_5
print (man)
print (boy)
print (woman)

# If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left.
names_x_6 = ("Marian", "Marosko", "Anicka", "Eva", "Martina", "Hanka")
(man, * family, woman,) = names_x_6
print(man)
print(family)
print(woman)

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop
names_x_7 = ("Marian", "Marosko", "Anicka", "Eva", "Martina", "Hanka")
for x in names_x_7:
    print (x)

# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number
names_x_8 = ("Marian", "Marosko", "Anicka", "Eva", "Martina", "Hanka")
for i in range (len(names_x_8)):
    print (names_x_8 [i])

# Using a While Loop
# You can loop through the list items by using a while loop
names_x_9 = ("Marian", "Marosko", "Anicka", "Eva", "Martina", "Hanka")
i = 0
while i < len (names_x_9):
    print (names_x_9[i])
    i = i + 1

# Join Two Tuples
this_is_tuple_9 = ("a", "b", "c", "d")
this_is_tuple_10 = ("1", "2", "3", "4")
this_is_tuple_11 = this_is_tuple_9 + this_is_tuple_10
print (this_is_tuple_11)
