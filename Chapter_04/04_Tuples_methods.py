# Here we will se some methods of tupples in working...

my_tup = (12, 13, 25.84, 42, "Harry", 29, 13)

# Counting no. of particular element in the tupple
print(my_tup.count(13))

# Checking the index value where this element is present 
print(my_tup.index(25.84))

# Adding two tupples together
my_tup2 = (25, "sohan", 23.45, 65, "shivam")
concatenation = my_tup + my_tup2
print(concatenation)

# Repeating a tupple multiple times
print(my_tup2 *3)

# Checking if a particular element exists in the tupple
print(25 in my_tup2)
print(24 in my_tup2)

# Length of the tupple
print(len(my_tup2))
print(len(my_tup))

# Slicing the tupple
print(my_tup2[1:4])

# Unpacking the tupple
my_tup3 = (25, "sohan", 23.45)
a, b, c = my_tup3
print(a, b, c)