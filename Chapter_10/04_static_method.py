# Here we will see use of static method in class.
"""Note we can use static method if we don't want to pass whole object to mehtods like (self)
   if our funcitons(methods) doesn't use them like here greet doesn't using them so instead of
   passing the whole self(object) to it, we made it a static method"""

class employee:
    language = "Python"
    salary = 1200000
    
    # This is static-method if you don't want to pass self(object) you can use this
    @staticmethod
    def greet():  
       print("Good morning.")

    def get_info(self): # cann't use for it as it uses the objec like(self.language)etc
        print(f"The language is: {self.language}, The salary is: {self.salary}")

harry = employee() # defining object to the class.

harry.greet()
harry.get_info()