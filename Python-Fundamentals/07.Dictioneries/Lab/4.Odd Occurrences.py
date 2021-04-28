data = [el.lower() for el in input().split()]
as_dict = {}
counter = 0
for word in data:
    if word in data:
        as_dict[word] = data.count(word)

for key, value in as_dict.items():
    if value % 2 == 1:
        print(key, end=" ")
