# Here we will see how to define class and then use it to create objects.
# the diff of preference btw class attribute and object attribut is cleared in next tut

class employee:
    # name = ""
    language = "Python"    # These are class attributes
    salary = 1200000


# Making object from the class(employee)
harry = employee()


# This is an object attribute
harry.name = 'Shivam' # type: ignore


# Printing object as default class attribute.
print("Printing object as default class attribute")
print(f"The language and salary of employee 1, harry is: {harry.language}, & {harry.salary}") 
print("Object attribute(Name):",harry.name) # type: ignore


# Modifing the class attributes in object and it will be prefered over class attributes
harry.language = "Javascript"    # These are Instance(object) attributes
harry.salary = 1000000



print("")
print("From here we will see how instance attribute is being preffered over class attribute")
print("")
# From here we will see how instance attribute is being preffered over class attribute



# This is an object attribute but being modified here
harry.name = "Rohan" # type: ignore


# Printing object after being modified by instance attribute
print("Printing object after being modified by instance attribute")
print(f"The language and salary of employee 1 after modification, harry is: {harry.salary}, & {harry.language}") 
print("Object attribute(Name)after modifiaction:",harry.name) # type: ignore


"""Note here 'name' is an object(instance) attribute they are created in object and belong to it,
   but language, and salary are class attributes and directly belong to class """


# and like Harry(object) we can multiple objects using the class employee