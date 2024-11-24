# Demonstration of different use case of (For loop)...


for i in range(0,4): # range(7) can also be used. 
    print(i)

print("\n")

# Printing the list till end using for loop
l = ["rohan", "satyam", 54] 
for item in l:    
    print(item)


print("\n")

# For loop with jump value.
for i in range(0, 20, 3):      # (start_loop, end_loop, Jmp_value)
    print(i)                   # jmp_value = how much value has to leave before printing next value


print("\n")

# For loop with else funciton 
l= ["start", "loop", "loop_exhasted"]             
for item in l: 
    print(item) 
else: 
    print("done") # this is printed when the loop exhausts! 

