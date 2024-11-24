# Here we will see how to use __inti__(self) constructor method...


class employee:
    # We don't need class attributes if want to initialize in object directly
    
    # Called dunder method, it's get automatically called when obj is defined
    def __init__(self, name, language, salary): 
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def get_info(self): # cann't use for it as it uses the objec like(self.language)etc
        print(f"The language is: {self.language}, The salary is: {self.salary}")


# harry = employee() # defining object attribute to the class, when init constructor is not used.
# harry.name = "Harry"
# harry.language = "Javascript"
# harry.salary = 1000000

# We can use _init_ constructor, give arg. to it and define object attribute directly like this
harry = employee("Harry", "Javascript", 1300000) 

print(harry.name, harry.language, harry.salary)

harry.get_info() # Calling the function with arg(harry)