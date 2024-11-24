# here we will see use of getter and setter methods. 
# @propery method is the getter, and     @(function name of property method).setter is the setter.

class employee:
    a = 5      # class attibute/property
    
    def __init__(self, name):
        self.name = name

    @classmethod        
    def show(cls):     # here we use 'cls' instead of 'self' cls= class 
        print(f"The value of class attribute will be: {cls.a}.  UNCHANGED")


#This is getter method it takes the output/attribute from the setter method and returns 
#(without setter it's only a read only method)
    @property                   
    def name(self):                       # define a method that behaves like an attribute
        return f"{self.fname} {self.lname}"
    

    @name.setter    #Set the properties or attribute to the name method. 
    def name(self, value):
        self.fname = value.split(" ")[0] #Split value(name here) where gets an(space),& make list out of it
        self.lname = value.split(" ")[1] #Here [0] indexing of list and set that value to self.f/lname here


o = employee("Shivam singh")
print(o.name)

o.a = 45
o.name = "Rohan Kumar"

print(f"The value of 'a' object is: {o.a} \nFull name is: {o.name}")
print(f"First name is: {o.fname} \nLast name is: {o.lname}")
