# warlus is a method in python by which we can assign values to variables as part of an expression

# Using walrus operator  (warlus operator = ':=' )

if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)")

else:
    print(f"Lenght of List is as expected ")

# here we are checking if the lenght of list given 'n' here is equal to the later value '3' here, 
# if it's true it print that. 