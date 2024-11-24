# here we will see how to enumerate list using enumerate func. 


l = [55, 65, 23, 48, 12]

# One way of doing it as:

index = 0
for item in l:
    print(f"The item at index {index} is {item}")
    index+=1
print("")
# but that's a very long process

# SO WE USE ENUMERATE FUNCITON:

for index,item in enumerate(l):
    print(f"The item at index {index} is {item}")
