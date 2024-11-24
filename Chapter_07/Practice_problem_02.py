"""Write a program to print the following star pattern. 
* * * 
*   *    for n = 3 
* * *  """

n = int(input("Enter the number you want to print star pattern:"))

for i in range(1, n+1):
    if(i==1 or i==n):
        print("* " * n, end="")       # The first and last row should print * n times
    else:
        print("*", end=" ")           # Print the first star with a space
        print("  " * (n-2), end="")   # Print (n-2) spaces between the stars
        print("*", end="")            # Print the last star
    print("")                         # Print a new line

 