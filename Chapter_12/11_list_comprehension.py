# here we will see how to modify a list using list COMPREHENSIONS 

l1 = [2, 5, 4, 1, 7]

# here to modify list, say we want to sqare every element in list and then move them to another list
l2 = []

# one way of doing this is:
for item in l1:
    l2.append(item*item)

print(l2)


# other way of doing is:
l3 = [item*item for item in l1]  

# Note: that type of practice make code more unreadable, so not use this frequently. 
# This is to understand if saw it somewhere

print(l3)
