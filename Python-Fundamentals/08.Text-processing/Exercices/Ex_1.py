data = input().split(", ")
result = []
for word in data:
    if 3 <= len(word) <= 16:
        if word.isalnum() or "-" in word or "_" in word:
            result.append(word)

word_to_print = '\n'.join(result)
print(word_to_print)