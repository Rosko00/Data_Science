# booleand and conjunction, disjunction, negation
# and / or / not

print (True and True) # True
print (False and False) # False
print (True and False) # False
print (False and False) # False

Iam_a_programer = True
print (Iam_a_programer)

# If the value of left operand is less than the value of right operand
bool_01 = 3 < 4
print (bool_01) # print is True

# If the value of left operand is greater than the value of right operand
bool_02 = 4 > 3
print (bool_02) # print is True

# If the values of two operands are equal, then the condition becomes true.
bool_03 = 54 == 54
print (bool_03) # Print is True
bool_04 = 32 == 31
print (bool_04) # Print is False

# If values of two operands are not equal, then condition becomes true.
bool_05 = 32 != 31
print (bool_05) # Print is True
bool_06 = 54 != 54
print (bool_06) # Print is False

# If both the operands are true then condition becomes true.
bool_07 = 3<4 and 6>5 
print (bool_07)  # Print is True
bool_08 = 3>4 and 6>5
print (bool_08) # Print is False

# If any of the two operands are non-zero then condition becomes true
bool_09 = 3>4 or 6>5
print (bool_09) # Print is True
bool_10 = 17!=14 or 4>6
print (bool_10) # Print is True

# Used to reverse the logical state of its operand.
bool_11 = not (4 < 15) and 5 > 7 
print (bool_11) # Print is False
bool_12 = not (4 < 15) or 5 < 7 
print(bool_12) # Print is True
bool_13 = not(3>6) or not(4==18 or 7>8)
print (bool_13) # Print is True
