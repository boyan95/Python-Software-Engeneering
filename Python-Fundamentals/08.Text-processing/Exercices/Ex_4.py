data = list(input())
result = []

for el in data:
    result.append(ord(el) + 3)
res = []
for el in result:
    res.append(chr(el))
print(''.join(res))