"""Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old...."""


def gen_tables(n):
    ptable = ""
    for i in range(1, 11):
        ptable += f"{n} X {i} = {n*i}\n"

    with open(f"CH_09_PP_tables/table_{n}.txt", "w") as f:
        f.write(ptable)


for i in range(2, 21):
    gen_tables(i)


