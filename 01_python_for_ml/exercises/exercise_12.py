text = "Machine Learning"

print(text[0])
print(text[-1])
print(len(text))
print(text[0:7])
print(text.upper())
print(text.lower())

text = "   Machine Learning is FUN   "

print(text.strip().lower())

text = "I am learning Java"

text = text.replace("Java", "Python")

print(text)
print(text.find("learning"))
print("Python" in text)

text = "Python,Machine Learning,Data Science"


languages = text.split(",")

print(languages)


result = " | ".join(languages)

print(result)