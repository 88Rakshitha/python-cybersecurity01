import os
path = input("Enter file path: ")
count = 0
for file in os.listdir(path):
    if file.endswith(".exe"):
        count+=1
print(".exe files found",count)        