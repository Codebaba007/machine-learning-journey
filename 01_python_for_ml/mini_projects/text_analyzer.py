text = input("Enter a sentence: ")

# Clean the text
text = text.strip().lower()

print()
print("Cleaned Text:", text)
print("Characters:", len(text))

# Count words
words = text.split()

print("Words:", len(words))

# Search for a word
word = input("\nEnter a word to search: ").lower()

print()
print("Word Found:", word in text)
print("Occurrences:", text.count(word))

# Replace the word
modified_text = text.replace(word, "***")

print("Modified Text:", modified_text)