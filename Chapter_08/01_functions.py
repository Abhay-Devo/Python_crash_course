# Here we will see how to create functions 



# CREATING THE FUNCTION
def avg():
    # This function will calculate the average of two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    avg = (num1 + num2 * num3) / 3
    print("Average is: ", avg)


# CALLING THE FUNCTION
avg()
