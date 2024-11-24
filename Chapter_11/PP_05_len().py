# this show us how to use len operator overloading in in class in python

class vector:

    def __init__(self, l):
        self.l = l
    
    def __len__(self):
        return len(self.l)
    
v1 = vector([5, 6, 3])
v2 = vector([4, 2, 7, 6, 5])
v3 = vector([9])

print(len(v1))
print(len(v2))
print(len(v3))