import re 

with open("123", "r") as file:
    text = file.read()
    print("File Components:\n", text,"\n")

words = len(text.split())

sentences = len(re.findall(r'[.!?]+(?:\s|$)', text))

uppercase = sum(1 for char in text if char.isupper())
lowercase = sum(1 for char in text if char.islower())

special_symbols = sum(1 for char in text if not char.isalnum() and char not in ' \t\n')

print(f"Words: {words}")
print(f"Sentences: {sentences}")
print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
print(f"Special symbols: {special_symbols}")
