"""Write a class “Calculator” capable of finding square, cube and square root of a 
number and Add a static method to greet the user... """


class calculator:
    def __init__(self, n) -> None:
        self.n = n

    def square(self):
        print(f"The Square is: {self.n * self.n}\n")

    def cube(self):
        print(f"The cube is: {self.n * self.n * self.n}\n")

    def square_root(self):
        result = round(self.n**(1/2), 3)        # Rounds to 3 decimal places
        print(f"The Squareroot is: {result} \n")

    @staticmethod
    def greet():
        print("Hello there,")

a = calculator(8)    # setting the object and passing the instance attribute.
a.greet()
a.square()
a.cube()
a.square_root()

