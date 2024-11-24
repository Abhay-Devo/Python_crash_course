# Here we will see how to pass arguments into a funtion, and what is default argument...

"""Default argumnet is an argument which will print the default value written with it 
    if any parameter is not passed related to it while calling the funtion"""



# Function with an argument
def greet(name):
    print(f"Good Morning, {name}")

greet("Harry")
print("")



# Function with a default argument
def Good_day(name, Ending="Thanks, Haryy bhai"): # Here "Ending" is a default argument
    print(f"Good day, {name}, {Ending}") 
    # print(Ending)

Good_day("Shivam")   # Func call with no parameter for default arg, here the value in default arg is printed
print("")

Good_day("Rohan", "Thank You") 
# Func call with parameter for default arg, here the value will be printed which is passed for default arg