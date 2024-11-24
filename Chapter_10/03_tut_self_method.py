# Here we will see use of self parameter method in class.


class employee:
    language = "Python"
    salary = 1200000


    # These are called self methods in python

    def get_info(self): # self is (para.), it could be named anything but (self) is prefered
        print(f"The language is: {self.language}, The salary is: {self.salary}")


    # Here (a) is the para but self is prefered and will encounter a warning if not use type:ignore
    def greet(a):  # type: ignore 
        print("Good morning.")


harry = employee() # defining object to the class.

harry.get_info() 
# employee.get_info(harry)      # both are same

""" For Now it will not work becoz now there no para given in the get_info() in class 
and when we call funciton here it get translated to= employee.get_info(harry) and harry here
is a argument passed to the get_info(), but currently the get_info does not take any arg. as 
in the class there is no parameter given to the get_info(), so we have to give it first..."""


# Now here we will change(modify) the class attribute & see what will happen
harry.language = "Javascript"
harry.salary = 1000000


harry.greet()
harry.get_info()