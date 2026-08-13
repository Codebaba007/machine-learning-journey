count = 0

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())
        count += 1

print("Total lines:", count)

try:
    with open("missing.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")