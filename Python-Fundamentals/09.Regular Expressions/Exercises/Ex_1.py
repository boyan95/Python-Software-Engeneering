import re

data = input()
pattern = r"\d+"
numbers = []
while data:
    match = re.findall(pattern, data)
    numbers.extend(match)
    data = input()

print(' '.join(numbers))

