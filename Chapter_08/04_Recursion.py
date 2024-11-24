# Here we will see how to use factorial in python...

def Factorial(n):
    if (n==1 or n==0):
        return 1
    return n * Factorial(n-1)


n = int(input("Enter the number you want factorial of:"))

print(f"Factorial of given number {n} is; {Factorial(n)}")


# Here we can also use loops to do that but this is also an way to solve the problem.