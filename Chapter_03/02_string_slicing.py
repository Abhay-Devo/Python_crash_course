# In this program we will see how we can slice a string in python

string1 = "Harry"

str_result = string1[0:3]   #[start_index:end_index] and this will define how much string will be sliced.

# Note: the string will be sliced from the start_index and will be executed till (end_index-1) as shown here...

print(str_result)
print(string1[-4:-1]) #Negative slicing just count the characters in negative order from the back of string.
print("Printing one character from the whole string:", string1[0])
print("Printing one character from the whole string:", string1[1])
print("Printing one character from the whole string:", string1[2])
print("Printing one character from the whole string:", string1[3])
print("Printing one character from the whole string:", string1[4])

print("\n")   # Both are same using different indexing one is (positive), other is (negative)

print("Printing one character from the whole string:", string1[-5])
print("Printing one character from the whole string:", string1[-4])
print("Printing one character from the whole string:", string1[-3])
print("Printing one character from the whole string:", string1[-2])
print("Printing one character from the whole string:", string1[-1])

print("\n")

print(string1[:4]) # It is as same as (string1[0:4])
print(string1[1:]) # It is as same as (string1[1:5]) here 5 in the place of end_index mean full length of string

print("\n")

string2 = "0123456789"
# Here string2[1:9:2] this means [start_index:end_index:jmp_char], 
# jmp_char means how many character you want to skip before printing the nex character of the string 

print("Print slice string while jumping few char in the string:",string2[1:10:2]) # Here end_index is 10-> python take string as (end_slice-1)
print("Print slice string while jumping few char in the string:",string2[1:9:3])
