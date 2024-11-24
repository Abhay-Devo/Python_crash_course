# Here we will see use of round function in this practice problem

"""The round function is used to round a floating number to the
    nearest integer or to a given number of decimal places.
    It can be used with positive or negative numbers.

    round(func(), 2/3/4/5) how many digits you want after decimal..."""


def f_to_c(f):
    return 5*(f - 32)/9


# Here we will see use of round function in this practice problem
f = int(input("Enter the tempreature in farenheit to convert it into degree celcius:"))


print(f"The temperature in degree celcius is: {round(f_to_c(f), 2)}")   # Directly printing the value

c = f_to_c(f)
print("The temperature in degree celcius is: ", round(c, 3))   # Printing the value after puting it into a var