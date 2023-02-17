VOWELS = ["a", "e", "i", "o", "u"]
text = input("Input: ")

text = ''.join([char for char in text if char.lower() not in VOWELS])
print(text)
