# This is multi-level Inheritance here we can create base class and child class at multiple level 
# like base-> child1-> child2-> child3.....


class employee:
    a = 1
    @staticmethod
    def greet():
        print("Hello there!!!")

class programmer(employee):
    b = 2 

class manager(programmer):
    c = 3


j = employee()
j.greet()
print(j.a)      # Print the attributes of only class employee
# print(j.b)      # Thow an error because it does not have attribute 'b'
print("")

k = programmer()
k.greet()
print(k.a)        # 'K' class has both a and b attribute becoz it is child of employeee
print(k.b)
print("")

l = manager()
l.greet()
print(l.a)        # 'l' class has all the attributes becoz it is child of programmer(which is child of employee)
print(l.b)
print(l.c)
