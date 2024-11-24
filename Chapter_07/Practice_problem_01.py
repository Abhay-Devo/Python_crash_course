"""Write a program to print the following star pattern. 
  * 
 *** 
*****  for n = 3 

    * 
   *** 
  ***** 
 *******
*********  for n = 5..."""

star = int(input("Enter the number you want star to print: "))

# End="" - here stops print to add new line as its default features
for i in range(1, star + 1):
    print(" "* (star-i), end="")                # This line prints space (star-1) times
    print("*"* (2*i-1), end="")                 # This line prints star (2*i-1) times
    print()                                     # print a new line after each row.

