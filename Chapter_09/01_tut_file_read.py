# Reading file using python file I/O function...

# open("filename", "mode of opening(read mode by default)")

f = open("ch_9_file_text_01.txt", "r")

text = f.read()      # read()= read the file all at once.
print(text)

f.close()            # Close()= closes the opened file (good practice)

print("")




# Reading file using readlines(), return the data of the file in the form of list...

f = open("ch_9_file_text_01.txt")

text = f.readlines()  # readlines()= read the file line by line and return the
print(text, type(text))

f.close()

print("")




# Reading file using readline(), this will read the text line by line
f = open("ch_9_file_text_01.txt") 

line1 = f.readline()  # readline()= read the file line by line (line1)
print(line1, type(line1))
line2 = f.readline()  # readline()= read the file line by line (line2)
print(line2, type(line2))
line3 = f.readline()  # readline()= read the file line by line (line3)
print(line3, type(line3))

f.close()

print("")




# Reading file using readline(), this will read the text line by line using WHILE()
f = open("ch_9_file_text_01.txt") 

line = f.readline()
while(line!=""):
    print(line)
    line = f.readline()

f.close()
