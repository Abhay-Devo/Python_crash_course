# Practice problem showing use of operator overloading and str() function in python 

class vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        # return vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return self.x + other.x, self.y + other.y, self.z + other.z   # CAN USE BOTH
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        # return f"({self.x}i + {self.y}j + {self.z}k)" 
        str_res =  vector(self.x, self.y, self.z)   # CAN USE BOTH
        return str_res
    
v1 = vector(5, 6, 3)
v2 = vector(4, 2, 7)
v3 = vector(7, 3, 5)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v2 + v3)
# we can do more 