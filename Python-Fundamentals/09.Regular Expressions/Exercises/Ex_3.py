import re

data = input()
searched = input()
word = rf"\b{searched}\b"

match = re.findall(word, data, re.IGNORECASE)

print(len(match))




