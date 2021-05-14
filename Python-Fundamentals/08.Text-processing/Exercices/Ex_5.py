data = input().split()
result = []
for word in data:
    if len(word) == 1:
        continue
    elif word[0] == ":" and not word[1] == ":" and len(word) == 2:
        result.append(word)
    elif word[0] == ":" and not word[1] == ":" and len(word) > 2:
        result.append(word[:2])

for_the_end = "\n".join(result)
print(for_the_end)
  #      : :: ::: :P :p ::p :::P