# Python dictionaries
# Dictionary items are ordered, changeable, and does not allow duplicates
dictionary_1 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter"}
print (dictionary_1)

# Dictionary Items
dictionary_2 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter"}
print (dictionary_2["Model"])

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key
dictionary_3 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", "Season": "summer"}
print (dictionary_3)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets
dictionary_4 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter",}
x = dictionary_4 ["Brand"]
# There is also a method called get() that will give you the same result
y = dictionary_4 . get ("Brand")
# The keys() method will return a list of all the keys in the dictionary
z = dictionary_4 . keys ()
print (x)
print (y)
print (z)

# The list of the keys is a view of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the keys list.
dictionary_5 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter",}
a = dictionary_5.keys ()
print (a)
dictionary_5 ["Type"] = "radial"
print (a)

# Get Values
# The values() method will return a list of all the values in the dictionary
dictionary_6 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter",}
b = dictionary_6.values()
print (b)
dictionary_6["Season"] = "summer"
print (b)

# Add a new item to the original dictionary, and see that the values list gets updated as well
dictionary_7 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
c = dictionary_7 . values ()
print (c)
dictionary_7 ["Dimension"] = "17"
print (c)

dictionary_8 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
d = dictionary_8 . items()
print (d)
dictionary_8 ["type"] = "radial"
print (d)

dictionary_9 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
if "Model" in dictionary_9:
    print ("Yes ' model is one the keys in the thisdict")
else:
    print ( "No 'model it is not ")

# Update Dictionary (Python - Change Dictionary Items)
# The update() method will update the dictionary with the items from the given argument
dictionary_10 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
dictionary_10 . update ({"Season": "summer"})
print (dictionary_10)

# Adding Items (Python - Add Dictionary Items)
# Adding an item to the dictionary is done by using a new index key and assigning a value to it
dictionary_11 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
dictionary_11 . update ({"Destination": "europe"})
print (dictionary_11)

# Removing Items (Python - Remove Dictionary Items)

# The pop() method removes the item with the specified key name
dictionary_12 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
dictionary_12 . pop ("Brand")
print (dictionary_12)

# The popitem() method removes the last inserted item 
# (in versions before 3.7, a random item is removed instead)
dictionary_13 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
dictionary_13 . popitem ()
print (dictionary_13)

# The del keyword removes the item with the specified key name
dictionary_14 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
del dictionary_14 ["Model"]
print (dictionary_14)
# The del keyword can also delete the dictionary completely

# The clear() method empties the dictionary
dictionary_15 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
dictionary_15 . clear ()
print ( dictionary_15)

# Python - Loop Dictionaries (Loop Through a Dictionary)
dictionary_16 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
for x in dictionary_16:
    print (dictionary_16[x])

# You can also use the values() method to return values of a dictionary
dictionary_17 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
for x in dictionary_17 . values ():
    print (x)
    
# You can use the keys() method to return the keys of a dictionary
dictionary_18 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
for x in dictionary_18 . keys ():
    print (x)

# Loop through both keys and values, by using the items() method
dictionary_19 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
for x, y, in dictionary_17 . items ():
    print ( x,y)

# Python - Copy Dictionaries (Copy a Dictionary)

# Make a copy of a dictionary with the copy() method
dictionary_20 = {"Brand": "Contiental", "Model": "Sport_Contakt_7", "Season": "winter", }
dictionary_copy_1 = dictionary_20 . copy ()
print (dictionary_20)
print (dictionary_copy_1)

# Python - Nested Dictionaries (Nested Dictionaries)
# A dictionary can contain dictionaries, this is called nested dictionaries
my_family_1 = {"children_1":{"name": "Hanka", "year": "2016"}, "children_2": {"name": "Marosko", "year": "2019"}}
print (my_family_1)

# Or, if you want to add two dictionaries into a new dictionary
children_3 = {"name": "Hanka", "year": "2016"}
children_4 = {"Name": "Marosko", "year": "2019"}
my_family_2 = {"children_3": children_3, "children_4": children_4}
print (my_family_2)
