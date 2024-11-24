def myfunc():
    print("Hello, World")


# If, Checking that is __name__ is equal to __main_, if yes then this code will run..
# means that the code below will not be run when we import this file into other program file

if __name__ =="__main__":
    print("Now, Inside of the if__name=='__main__': funciton")
    myfunc()
    
    print(__name__)   # tells about the file its currently running in(is it main or any other file(imported))