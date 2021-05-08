# This is a sample Python script.

import os

for file in os.listdir("C:\Python_Class\Python_Notes"):
    if file.endswith(".txt"):
        file_path = os.path.join("C:\Python_Class\Python_Notes", file)
        print(file_path)
        file_size = os.stat(file_path)
        print("Size of file :", file_size.st_size, "bytes")