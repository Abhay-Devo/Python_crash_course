# Normally we have to first open the file do my work into that, and then close it,
# but with 'with' keyword, we don't have to do that. It automatically opens and
# closes the file for us.

f = open("ch_9_file_text_01.txt", "r")

text = f.read()      # read()= read the file all at once.
print(text)

f.close()            # Close()= closes the opened file (good practice)

print("")



# Using with statement...
with open("ch_9_file_text_01.txt", "r") as f:
    text = f.read()
    print(text)
    # The file is automatically closed after we are done with it.