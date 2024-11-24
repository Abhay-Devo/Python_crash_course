"""Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user..."""


marks1 = int(input("Enter your marks for Science:"))
marks2 = int(input("Enter your marks for Maths:"))
marks3 = int(input("Enter your marks for English:"))


total_percentage = 100*(marks1 + marks2 + marks3)/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("\nYou have passed the exam!!!")
    print("Your total percentage is:", total_percentage)

elif(total_percentage>100 or marks1>100 or marks2>100 or marks3>100):
    print("\nInvalid marks. Marks cannot be more than 100.")

else:
    print("\nYou have failed the exam!!!")
    print("Your total percentage is:", total_percentage)