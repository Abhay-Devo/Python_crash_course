# Here we will see how to make a program that calculates the sum of first n natural numbers using recursion...


def sum_recursion(n):
    if (n==1):
        return 1
    return sum_recursion(n-1) + n


# Here we are calling the function with n=5 to see the result

n = int(input("Enter the number you want to calulate the of natural no.:"))
print(sum_recursion(n))