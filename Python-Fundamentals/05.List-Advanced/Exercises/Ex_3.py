data = [int(i) for i in input().split(".")]


data[-1] += 1
if data[-1] > 9:
    data[-1] = 0
    data[-2] += 1
if data[-2] > 9:
    data[-2] = 0
    data[-3] += 1

res = [str(i) for i in data]
result = ".".join(res)
print(result)