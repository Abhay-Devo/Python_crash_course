# just like type def we can also tell the type of variable we are creating to a list, dict, tupple, union...


from typing import Tuple, List, Union, Dict    # etc


#  List of integers
l1 : list[int] = [5, 6, 2, 6, 7]
l2 : list[str] = ["harry", "rohan", "shivam", "krishna"]
l3 : list[float] = [5.23, 6.25, 7.00, 4.98]


# Union type for variables that can hold multiple types used with list
union_list : list[Union[str, int]] = ["harry", 5, "rohan", 2, "shivam", 9, "krishna"]


# Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123" 
identifier = 12345  # Also valid


# Tuple of a string 
t1_1 : tuple[str] = ("harry",)
t1_2 : tuple[str, ...] = ("harry", "rohan", "shivam") # for multiple  str type  tupple(only for single type)


# Tuple of integer
t2_1 : tuple[int] = (5,)
t2_2 : tuple[int, ...] = (5, 6, 9, 4)    # for multiple int type tupple(only for single type)


# Tuple of str and int combined
t3 : tuple[str, int] = ("harry", 4)
# t3_2 : tuple[str, int, ...] = ("harry", 4, "rohan",5, "shivam", 6)   # doesn't work for this 



# Dictionary with integer keys and string values
d1 : dict[int, str] = {1:"shivam", 2:"rohan", 3:"krishna"}

