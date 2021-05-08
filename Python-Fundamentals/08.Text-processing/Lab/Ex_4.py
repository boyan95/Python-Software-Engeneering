band_word = input().split(", ")
text = input()
for word in band_word:
    text = text.replace(word, "*" * len(word))

print(text)
