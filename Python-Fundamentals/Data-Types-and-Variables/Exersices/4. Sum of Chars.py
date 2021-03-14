n = int(input())
res = 0

for ch in range(n):
    data = input()
    res += ord(data)

print(f"The sum equals: {res}")