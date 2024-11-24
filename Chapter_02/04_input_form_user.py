""" Taking Inputs from users and then work on it..."""

inp1 = int(input("Enter the first number:"))
inp2 = int(input("Enter the second number:"))
print("\n")

print("The first number is:", inp1)
print("The Second number is:", inp2)

print("The sum of both the numbers 'inp1 + inp2' is:", inp1+inp2)
print("\n")


""" Here both the numbers will not be added, instead they will be 
    joined as they were because input() in default interpret every user input as a string."""

inp3 = input("Enter the first number:")
inp4 = input("Enter the second number:")
print("\n")

print("The first number is:", inp3)
print("The Second number is:", inp4)

print("The sumup of both the numbers 'inp3 + inp4' is:", inp3+inp4)

