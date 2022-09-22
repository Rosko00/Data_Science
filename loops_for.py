# Python For Loops
# With the for loop we can execute a set of statements, once for each item in a list

# We can go through fields using a cycle
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print (number)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  # print in fruit in a fruit list

# or via strings
for Iam in "Marian Galik":
    print (Iam)

# With the break statement we can stop the loop before it has looped through all the items
for x in fruits:
    print (x)
    if x == "banana":
        break

# Exit the loop when x is "banana", but this time the break comes before the print:
for x in fruits:
    if x == "banana":
        break
    print (x)

# With the continue statement we can stop the current iteration of the loop, and continue with the next
for x in fruits:
    if x == "banana":
        continue
    print (x)

# To loop through a set of code a specified number of times, we can use the range() function
# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number
for x in range (6):
    print (x)

# The range() function defaults to 0 as a starting value, 
# however it is possible to specify the starting value by adding a parameter

for x in range(2,6):
    print (x)

# The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by adding a third parameter

for number in range(0, 10, 2):
    print(number)

for x in range (2,30,3):
    print (x)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished

for number in range (10):
    print (number)
else:
    print ("Finaly finished!")

for x in range (10):
    if x == 7: break
    print (x)
else:
    print("Finaly finished!")

# Nested Loops
tropical_fruit = ["banana", "mango", "lemon"]
homemade_fruit = ["apple", "chery", "strawberries"]
for x in tropical_fruit:
    for y in homemade_fruit:
        print ("double ice cream:", x,y)
