# loops while
# While loop has a condition in it and works similar to if
# With the while loop we can execute a set of statements as long as a condition is true

counter = 0
while counter < 41:
    print (counter)
    counter += 1

counter = 0
while True:
    print (counter)
# infinite cycle
    if counter >= 5:
        break
    counter +=1

# The continue keyword is used to prematurely end the iteration, but not the entire cycle
counter = 0
while True:
    if counter == 2:
        counter += 1
        continue
    if counter >= 5:
        break
    print (counter)
    counter += 1

# We can use it again in the for loop
for i in [1,2,3,4,5]:
    if i == 2:
        continue
    print (i)
    
# With the else statement we can run a block of code once when the condition no longer is true
numbers_1 = 1
while numbers_1 < 10:
    print (numbers_1)
    numbers_1 += 1
else:
    print ("numbers_1 is no longer less than 10")
