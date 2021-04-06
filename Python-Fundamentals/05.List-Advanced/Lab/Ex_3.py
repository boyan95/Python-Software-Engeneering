line = input().split()
key_word = input()

result = [el for el in line if el == el[::-1]]
counter = [el for el in line if el == key_word]

print(result)
print(f"Found palindrome {len(counter)} times")
