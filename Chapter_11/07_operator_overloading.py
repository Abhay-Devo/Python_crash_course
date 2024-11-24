# Trying to create your own arthematic opertion method to customize 
# the behavior of those operations for instances of the class

class number:

    def __init__(self, num):
        self.num = num

# These functions allows us to define custom behaviour for our attributes and helps us in encapsulation.
# Like for example when to perform these function on obj, we don't have to write e.g(a.num + b.num) etc

    def __add__(self, other):
        return number(self.num + other.num)   
    # Note: If want to work on more than two attributes use return number(__ + __). else use simple one
    
    def __sub__(self, other):      
        return self.num - other.num 
    
    def __mul__(self, other):     # Here other parameter takes the other para than self argument(here 'b')
        return self.num * other.num
    
    def __truediv__(self, other):
        return self.num / other.num
    
    def __floordiv__(self, other):
        return self.num // other.num
    
    def __str__(self):    # Have to use str method if using 2+ attribute else output will be hex-code
        return f"The number in object 'a' is: {self.num}"
 
    
a = number(8)
b = number(4)
c = number(3)

result = a + b + c
print(str(result))
print("\n")

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(str(a))
