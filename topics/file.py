# File Handling

with open("text.txt", "w") as file:
    file.write("This Is File Handling Class")
    file.close()
    

file = open("text2.txt", "w") 
file.write("This Is File Handling Class With type 2")
file.close()

# 3 Ways to Read the File

# file =open("text3.txt", "r") -> This will give Error
file = open("text2.txt", "r")
for line in file:
    print(line)

file = open("text2.txt", "r")
print(file.read())
    
with open("text2.txt", "r") as file:
    for line in file:
        print(line)