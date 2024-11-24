# Here we will see how we can use return to take output from our funtion to the main program...

def Check_ret(name, Ending="thanks"):
    greet = "Good Morning, " + name + Ending
    return greet

# Here we are directly printing the output without string it.
print("Printing the return value:", Check_ret("Rohan ","Giving Ending"))


# Here we are calling the function and storing the output in a variable
Ret_Val_Container = Check_ret("Mohan ")
print(Ret_Val_Container)




# Another example to return some integer.
def avg():
    # This function will calculate the average of two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    avg = (num1 + num2 * num3) / 3
    return avg

store_return = avg()
print("The average of those three numbers is:", store_return)