# IF-ELSE coditionals statement


age = int(input("Enter your age to check if you're concent or not:"))

# If statement-1
if(age%2==0):
    print("Even number")


#Both are independent from each other 

# If statement-2
if (age>18): # if condition1 is True 
    print ("Yes, You have the concent") 
        
elif(age<=0): # if condition2 is True  
    print("Please enter a valid age") 
 
else:             # otherwise 
    print("No, You not have concent") 

print("End of program")