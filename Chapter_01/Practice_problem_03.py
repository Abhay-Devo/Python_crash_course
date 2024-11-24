# This program demonstrate how to access any directory from the system using OS Module...

import os

directory_path = 'C:\\Users\\HP\\OneDrive\\Desktop\\C_course'

contents = os.listdir(directory_path)

for items in contents:
    print(items)