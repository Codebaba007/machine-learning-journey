

with open("Example.txt","r") as file:
    content = file.read()

print(content) 

with open("example.txt", "w") as file:
    file.write("Python\n")
    file.write("Machine Learning\n")
    file.write("Data Science\n")
print(content)

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
print("\n")
with open("example.txt", "r") as file:
    first_line = file.readline()

print(first_line)        

with open("example.txt", "r") as file:
    lines = file.readlines()

print(lines)

with open("example.txt", "a") as file:
    file.write("Deep Learning\n")

