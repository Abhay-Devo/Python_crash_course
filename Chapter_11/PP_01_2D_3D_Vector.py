class twodvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2D vector is: {self.i}i + {self.j}j")

class threedvector(twodvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)    # Using super/parent classes attribute directly without setting them again
        self.k = k

    def show(self):
        print(f"The 2D vector is: {self.i}i + {self.j}j + {self.k}k")


a = twodvector(5, 4)
b = threedvector(2, 3, 6)

a.show()
b.show()