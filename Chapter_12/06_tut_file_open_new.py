# Here will will open and read two file at a same time using with function


with (
    open('ch_9_file_text_01.txt') as f1, 
    open('ch_9_file_text_02.txt') as f2
): 
 
    data1 = f1.read()
    data2 = f2.read()

    print(data1)
    print(data2)


