# here we will see how to handle exception and also to raise one...

try: 
   # Code which might throw exception  
   num = int(input("Enter a number:"))

except Exception as e:  
    print(e)              # default message from exception (general exception, exception not known)
    print("Please enter a valid input!!!") # exception handling with mannual message


# For certain type of exception (when exception is known) 
# note if other type of exception came (code crash)
try:
    div = (25/0)
except ZeroDivisionError:
    print("Cann't divide with zero!!!")
print("This code will run even if the exception is raised")



# Raising an exception...
check = int(input("Enter a number:"))
if(num<5):
    raise Exception("Please enter a number greater than 5!!!") # we can write custom message with it.

else:
    print("code will not run!!!") # if we use raise, and exception occur the program will throw an error