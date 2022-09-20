# Conditions

# These conditions can be used in several ways
is_marian = True
if is_marian == True:
    print ("He is a programer")

number_1 = 33
number_2 = 200
if number_2 > number_1:
    print ("number_2 is greater that number_1")

Iam_teacher = True
if Iam_teacher == False:
    print ("He is a teacher")
else:
    print ("He is not a teacher")

# if the previous conditions were not true, then try this condition
number_3 = 33
number_4 = 33
if number_4 > number_3:
    print("number_4 is greater that number_3")
elif number_4 == number_3:
    print("number_4 and number_3 are equal")
else:
    print ("not result")

# Every number != 0 has an implicit truth value of True

if 1:
    print ("Its True") # print is True
else:
    print ("Its False")

if 0:
    print("Its True")
else:
    print("Its False") # print is False

if 2:
    print("Its True") # print is True
else:
    print("Its False")

if -2:
    print("Its True") # print is True
else:
    print("Its False")

# Attention, this does not apply
print (1 == True) # print is True
print (0 == False) # print is True
print (2 == True) # print is False
print (-2 == True) # print is False

# The and keyword is a logical operator, and is used to combine conditional statements

age = 41
number_5 = number_1 # 33
number_6 = number_2 # 200
if age > number_5 and number_6 > number_5:
    print("conditions are True")
else:
    print("conditions are False")

# The or keyword is a logical operator, and is used to combine conditional statements

age = 41
number_5 = number_1  # 33
number_6 = number_2  # 200
if age > number_5 or age > number_6:
    print("conditions are True")
else:
    print("conditions are False")

# You can have if statements inside if statements, this is called nested if statements

age = 41
if age > 10:
    print ("above ten,")
    if age > 20:
        print ("and also above 20,")
        if age > 30:
            print ("and also above 30,")
            if age > 40:
                print ("and also above 40")
                if age > 50:
                    print ("and also above 50")
                else:
                    print("but not above 50.")
