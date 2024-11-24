# Note used much since f string comes from version 3.10
# do similar things like f string 

a = "{} is a good {}".format("Shivam", "boy")  # defult will be like index{0}, {1}, {2}
print(a)
# but can also assign index  as wanted like:

b = "{1} is a bad {0}".format("shivam", "boy") # can change the order by indexing 
print(b) 

b1 = "{1} is a bad {1}".format("shivam", "boy") # can give similar index to points
print(b1) 