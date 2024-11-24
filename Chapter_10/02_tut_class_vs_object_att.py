# Here we will see which attribute get prefrence 
# (means get executed if both are defined for same object)


class employee:
    # name = ""
    language = "Python"    # These are class attributes
    salary = 1200000


# Making object from the class(employee)
harry = employee()


print(harry.language, harry.salary) # Printing the class attribute


# Now here we will change(modify) the class attribute & see what will happen
harry.language = "Javascript"
harry.salary = 1000000

print(harry.language, harry.salary) # Printing the instance attributes and they will be prefered