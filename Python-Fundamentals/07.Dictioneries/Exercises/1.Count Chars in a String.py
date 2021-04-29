command = list(input())
result = {}

for char in command:
    if char == " ":
        continue
    else:
        result[char] = command.count(char)
for key, value in result.items():
    print(f"{key} -> {value}")