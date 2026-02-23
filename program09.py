
file01 = input("Enter file name: ")
try:
    with open(file01, "r") as file:
        content = file.read() 
        print(content) 
except FileNotFoundError:
    print("File not found.......")
