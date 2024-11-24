# here we will see use of lamda function which is used to create one liner function...

# normal function
def square(x: int)-> int:
    return x*x

print(square(5))


# By using Lambda:
result = lambda x: x*x
print(result(5))