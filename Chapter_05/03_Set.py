# A set is an unordered collection of unique elements(no repetetion allowed).
# But if we pass repetetive value it will only accept one and ignore other not matter how many they are.
# Sets are mutable, meaning that they can be modified after creation.


set_a = {1, 5, 9, 12, 20.25,"Shivam"}  # This is a set uses curly braces as dict but only contain values not key-value pair 


# To create an empty set,
emp_dic = {}      # This will create an empty dictionary not an empty set for that:
emp_set = set()   # This will create an empty set 


# Let's see how set stops repetetiveness 
set_a = {1, 1, 5, 8, 4, 1.95,"Rohan"}
print(set_a)                # Only print '1' once 