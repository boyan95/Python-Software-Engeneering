n = int(input())
data = {}
for num in range(n):
    word = input()
    synonym = input()
    if not word in data:
        data[word] = synonym
    else:
        data[word] += f", {synonym}"

for el in data:
    print(f"{el} - {data.get(el)}")