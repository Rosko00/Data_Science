# strings
string = "This is a string"
apple = 365
print (string)
print (1)
print (1.5)
print (True)
print (apple)
print ("Primary string")

# introduction in string
string_01 = 'This is a string \' this is the second string'
print (string_01)

# new line in string
string_02 = 'This is a string \n This is a string on a new line'
print (string_02)

# this is \t tab
string_03 = 'This is a string \t This is a string using a tab'

# addition string
string_04 = 'Marian' + 'Galik'
print (string_04)
string_name = 'Marian'
string_surname = 'Galik'
print (string_name + string_surname)

# multiplication string
string_05 = 5 * 'Marian'
print (string_05)

# addition string and integer
string_06 = 'This is a string', 10, 'This is the second string'
print (string_06)
print ('This is a string' + str(6))
print (type(6)) # clas 'integer'
print (type(str(6))) # class 'string'

# concatenation of strings using an index,
name = 'Marian Galik'
print (name[0])  # print in 0
print (name[6])  # print in space
print (name[-1]) # print in k
print (name[-2]) # print in i

# concatenation of strings using an composite index
print (name[0:6])  # print in Marian
print (name[ :6])  # print in Marian
print (name[ :-1]) # print in Marian Gali
print (name[ :2])  # Print in Ma
print (name[-4: ]) # Print in alik

print (name[2:103]) # print in rian Galik
print (name[104:0])  # print in nothing




