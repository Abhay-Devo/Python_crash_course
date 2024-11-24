# Write a python program to replace some words form the given string...

letter = '''
    Dear <|Name|>,
    You are selected
    <|Date|>
    '''
name_inp = input("Enter your Name to replace in the letter:")
date_inp = input("Enter the Date to replace in the letter(format=dd/mm/yyyy):")

name_inp = name_inp.title()

# letter = letter.replace("<|Name|>",name_inp )
# letter = letter.replace("<|Date|>",date_inp )
#print(letter)


# Or can use this both are same
print(letter.replace("<|Name|>",name_inp ).replace("<|Date|>",date_inp ))

# Note: This will not change the main string as my previous program was doing 
# (it's just making copy of the main string and printing it.)
