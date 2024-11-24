""" This program will demonstrate different types of operations in python programming..."""

a = 3
b = 5 

# ARITHEMATIC OPERATIONS

print("ARITHEMATIC OPERATORS:\n")
print("Addition of a and b is:", a + b)
print("Subtraction of a and b is:", a - b)
print("Multiplication of a and b is:", a * b)
print("Division of a and b is:", a / b)
print("Modulus of a and b is:", a % b)
print("Exponentiation of a and b is:", a ** b)
print("Floor Division of a and b is:", a // b)
print("\n")


# ASSINGNMENT OPERATIONS

print("ASSINGNMENT OPRERATOR:\n")
c = 5 
d = c
print("Value of c is:", c)
print("Assigning the value of 'c' variable to 'd' variable:", d)

d+=3     #Incrementing the value of d by 3
print("Value of 'd' variable after addition of 3:", d)

c-=1    #Decrementing the value of c by 1
print("Value of 'c' variable after subtraction of 1:", c)

a*=2    #Mulitplying the value of a by 2
print("Value of 'a' variable after multiplication of 2:", a)

b/=2    #dividing the value of b by 2
print("Value of 'b' variable after division of 2:", b)
print("\n")


# COMPARISON OPERATIONS

print("COMPARISON OPERATORS:\n")
print("Is 'c' variable equal to 'd':", c==d)          #Checking if equal to.
print("Is 'c' variable not equal to 'd':", c!=d)      #Checking if not equal to.
print("Is 'c' variable greater than 'd':", c>d)       #Checking if greater than/ could by greater than equal to(>=)
print("Is 'c' variable lesser than 'd':", c<d)        #Checking if lesser than/ could by lesser than equal to(<=)
print("\n")



# LOGICAL OPERATIONS

print("LOGICAL OPERATORS:\n")
print("Not with true Boolean will print:",not(True))
print("Not with false Boolean will print:",not(False))
print("\n")

#truth table of 'or'
print("Truth table of 'or' for True or False:",True or False)
print("Truth table of 'or' for True or True:",True or True)
print("Truth table of 'or' for False or False:",False or False)
print("Truth table of 'or' for False or True:",False or True)
print("\n")

#truth table of 'and'
print("Truth table of 'and' for True and False:",True and False)
print("Truth table of 'and' for True and True:",True and True)
print("Truth table of 'and' for False and False:",False and False)
print("Truth table of 'and' for False and True:",False and True)
print("\n")

