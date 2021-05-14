data = input().split()
sum = 0
if len(data[0]) == len(data[1]):
    for el in range(len(data[0])):
        sum += ord(data[0][el]) * ord(data[1][el])
elif len(data[0]) >= len(data[1]):
    for el in range(len(data[1])):
        sum += ord(data[0][el]) * ord(data[1][el])
    for el in data[0][len(data[1]):]:
        sum += ord(el)
elif len(data[0]) <= len(data[1]):
    for el in range(len(data[0])):
        sum += ord(data[1][el]) * ord(data[0][el])
    for el in data[1][len(data[0]):]:
        sum += ord(el)

print(sum)