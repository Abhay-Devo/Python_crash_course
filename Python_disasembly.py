import dis

def func():
    a = int(input("Enter the first no.:")) 
    b = int(input("Enter the second no.:")) 
    return (a+b)

dis.dis(func)