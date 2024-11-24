# here we will see use of super method()
# Super method() helps you to access the methods or property of the parent/super class


class employee:
    name = "Harry"           #  Property/attribute of class
    def __init__(self) -> None:
        print("Constructor function of employee")
    a = 1

class programmer(employee):
    def __init__(self) -> None:
        print("Constructor function of programmer")
        super().__init__()          # Run the constructor of parent(super) class(employee)
    b = 2 

class manager(programmer):
    def __init__(self) -> None:
        print("Constructor function of manager")
        super().__init__()          # Run the constructor of parent(super) class(programmer)
    c = 3


# j = employee()
# print(j.a)  


# k = programmer()
# print(k.a)
# print(k.b)


# So even though both 'j' and 'k' objects are commented there constructor will run because of super() func
l = manager()
print(l.a)
print(l.b)
print(l.c)
