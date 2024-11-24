# Here we will see some methods that are used with dictonary 

marks = {
    "rohan" : 100,
    "arjun" : 50,
    "sachin" : 35
}


emt_dict = {}      # This will create an empty dictionary


# Printing items from the dictionary
print(marks.items())

# Printing the keys from the dictionary
print(marks.keys())

# Printing the values from the dictionary
print(marks.values())

# Updating the existing item from the dictionary
marks.update({"sachin":40})
print(marks)

# Updating (adding) new item into dictionary
marks.update({"saurav": 90})           # can be done both update and add new item at same time using ',' btw
print(marks)                           # Like this marks.update({"sachin":40 , "saurav": 90})


# Length of dictionary
print(len(marks))


# Removing an item from the dictionary
del marks["arjun"]          # Arjun item will be deleted
print(marks)                           


# or we can use pop() method to remove an item from the dictionary
# pop() method will return the value of the item that is removed from the dictionary
print(marks.pop("sachin"))  # Sachin item will be deleted and value will be returned as here
print(marks)


# Getting something from the dictionary
print(marks.get("rohan"))       # Its diff from print(marks["rohan"]) if unidentified key entered will throw error
print(marks.get("Shivam"))      # If unidentified key is entered will return 'NONE' not error



# The popitem() method removes and returns an arbitrary element from the dictionary(Last-in First-out order). 
# If the dictionary is empty, it raises a KeyError.
marks.popitem()
print(marks)
