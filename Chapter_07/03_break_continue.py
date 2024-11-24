# Here we will see use of BREAK statement, CONTINUE statement, PASS statement...


# BREAK STATEMENT.
for i in range (0,80): 
    if (i==3):        # will Break the loop when the condition is met
        break
    print(i)     # this w ill print 0,1,2 and 3 


# CONTINUE STATEMENT.
for i in range(4): 
    print("printing") 
    if (i == 2):   # if i is 2, this particular iteration is skipped  and loop will go again to check condition
        continue 
    print(i) 


# PASS STATEMENT.
l = [1,7,8] 
for item in l: 
    pass      # without pass, the program will throw an error, helps to leave loop or func() without any declaration
  
