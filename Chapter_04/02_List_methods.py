# In this program we will see some methods used inn lists


l1 = [45,34,56,76,1,5,10]

# Append in the given list at the end 
l1.append(43)
print(l1)

# Append the list at given index
l1.insert(3, 90)     # format for insert (index_position, value) 
print(l1)

# Sorting the given list
l1.sort()
print(l1)

# Reversing the given sorted list
l1.reverse()
print(l1)


# Poping out the value from the list and then print the list
l1.pop(3)
print(l1)

# Printing the poped value from the list
value = l1.pop(3)
print(value)


# Removing a value from the string
l1.remove(1)
print(l1)
