# Lists are Mutable datatype in python...
# Here we will see how to create and use Lists
# They are muttable unlike strings (means can be changed using indexing)


friends = ["Apple", "Orange", 345, 23, 324.35, "rohan"]

# Printing list throught indexing
print("Printing list at index[0] in list(friend)",friends[0])
print("Printing list at index[2] in list(friend)",friends[2])
print("Printing list at index[4] in list(friend)",friends[4])


# Changing List through Indexing (list are mutable)
friends[2] = "Mango"
print("Printing list after changing index[2] in list(friend)",friends[2])


# Printing list though slicing just like strings
print("Printing list from index[1] to index[4] in list(friend)",friends[1:4])


