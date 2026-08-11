# Day 12 — String Manipulation

# Strings are sequences of characters.

text = "Machine Learning"

# Indexing
print(text[0])
print(text[-1])

# Slicing
print(text[0:7])

# Length
print(len(text))

# Case conversion
print(text.upper())
print(text.lower())
print(text.title())

# Removing whitespace
name = "   Mehedi   "
print(name.strip())

# Replacing text
print(text.replace("Machine", "Deep"))

# Searching
print("Learning" in text)

# Finding position
print(text.find("Learning"))

# Splitting
languages = "Python,Java,C++"
print(languages.split(","))

# Joining
languages_list = ["Python", "Java", "C++"]
print(", ".join(languages_list))

# Counting
print("banana".count("a"))

# Start and end checks
print(text.startswith("Machine"))
print(text.endswith("Learning"))

# f-string
name = "Mehedi"
age = 23

print(f"My name is {name} and I am {age} years old.")