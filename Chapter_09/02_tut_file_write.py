# Here we will see how to write into any file using write function...

st = "This string will be written inside a file using write function()"

f = open("ch_9_file_text_02.txt", "a")
f.write(st)        # Write()= used to write inside any file,
f.write("writing something direclty") # will replace everything written before
f.close()



# Using Append mode of file I/O to add something in the last of the file
f = open("ch_9_file_text_02.txt", "a")

f.write("next line direct string")   # Add in the last of the file 
f.write(st)

f.close()
