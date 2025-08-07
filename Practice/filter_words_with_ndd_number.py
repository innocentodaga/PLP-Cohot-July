# List of words
words = ["apple", "banana", "kiwi", "grape", "orange", "fig", "plum"]

# List comprehension to get words with odd lengths
odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Words with odd number of characters:", odd_length_words)
