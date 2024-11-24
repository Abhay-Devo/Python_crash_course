# Here we will see how to merge dictionary in a new way..(using '|' operator)

dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c': 4} 
merged = dict1 | dict2 

print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4} 