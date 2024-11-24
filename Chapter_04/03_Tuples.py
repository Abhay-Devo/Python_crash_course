# tupples are Immutable datatype in python

# tupples are ordered collection of immutable python objects
a = ("rohit", 34, 35346, 34.54,"shivam")
print(type(a))


b = (23,)  # If want to make tupple with only one value in it, put a comman later otherwise interpreted as int
c = (43)   # Interpreted as integer

print(type(b))
print(type(c))


# b[1] = "rohan" # Not possible tupples cannot be changed they are immutable
