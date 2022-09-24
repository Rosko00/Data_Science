# functions in python
# function is a block of code which only runs when it is called
# you can pass data, known as parameters, into a function
# function can return data as a result

# In Python a function is defined using the def keyword
def my_function ():
    print ("Hello from a function")
my_function ()

def addition (number_1, number_2):
    print (number_1 + number_2)
addition (5,4)

def addition_1 (number_3, number_4):
    result = number_3 + number_4
    return result
result = addition_1 (number_3 = 5, number_4 = 4)
print ("the result", result)

def addition_3 (number_5, number_6):
    result = number_5 + number_6
    return result
result = addition_3(addition_3(addition_3(addition_3("Marian" , " Galik"), " is"), " the"), " best")
print ("who am I", result)

def addition_4 (number_7, number_8):
    result = number_7 + number_8
    return result
x = ( 5 + 4 ) +3
result = addition_4 (addition_4 (number_7 = 5, number_8 = 4), 3)
print (result)
     
# Arguments
# The following example has a function with one argument (fname). 
# When the function is called, we pass along a first name, 
# which is used inside the function to print the full name
def my_function_1 (frst_name):
    print (frst_name + " Galik")
my_function_1 ("Marian")
my_function_1 ("Hanka")
my_function_1 ("Marosko")

# Number of Arguments
# By default, a function must be called with the correct number of arguments
def my_function_2 (frst_name, last_name):
    print (frst_name + "" + last_name)
my_function_2 ("Marian", " Galik" )

# If the number of arguments is unknown, add a * before the parameter name:
def my_function_3 (*kids):
    print ("The youngest child is" + kids [2])
my_function_3 (" Marian", " Hanka", " Marosko")

# Keyword Arguments
def my_function_4 (children_3, children_2, children_1):
    print ("The youngest child is" + children_3)
my_function_4 (children_1 = " Marian", children_2 = " Hanka", children_3 = " Marosko")

# Default Parameter Value
# The following example shows how to use a default parameter value
# If we call the function without argument, it uses the default value
def my_function_5 (country = " Slovakia"):
    print ("I am from" + country)
my_function_5 (" Sweden")
my_function_5 (" Finland")
my_function_5 ()
my_function_5 (" Brazil")

# Return Values
def my_funcion_6 (x):
    return 5 * x 
print (my_funcion_6 (3))
print (my_funcion_6 (6))
print (my_funcion_6 (9))


number = list (range(0,10))
print (number)
def sum_array (array):
    result = 0
    for number in array:
        result += number
    return result
print (sum_array(number))

def simple_sum (a,b):
    return a +  b 
if simple_sum (4,3) > simple_sum (5,2):
    print ("First is bigger")
else:
    print ("Second is bigger")
 
def simple_sum(a, b):
    return a + b
temp = [simple_sum(3,4), simple_sum (simple_sum(1,2), 3)]
print (temp)
