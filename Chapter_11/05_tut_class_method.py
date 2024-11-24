# here we will see use of class methods

class employee:
    a = 5      # class attibute/property

    def norm_show(self):
        print(f"The value of attribute after change in object is: {self.a}")


    # Stops the object to change the value of class attribute in that object
    @classmethod        
    def show(cls):     # here we use 'cls' instead of 'self' cls= class 
        print(f"The value of class attribute is: {cls.a}.  UNCHANGED")


"""Note: obj.a = 10 will only change the value of a for this particular obj, 
        but for other object the value will be default..."""

obj = employee()

obj.a = 10     # object/instance attibute

obj.norm_show()     # the value of 'a' attribute from class is changed due to modification for this object
obj.show()        # But here there will be no effect of class atttribute modification in obj becoz of (@classmethod)


print("")
sec_obj = employee()
sec_obj.norm_show()
sec_obj.show()