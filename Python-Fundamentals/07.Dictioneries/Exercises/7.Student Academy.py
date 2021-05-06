num = int(input())
result = {}

for _ in range(num):
    key = input()
    value = float(input())
    if key not in result:
        result[key] = []
    result[key].append(value)

for key, value in result.items():
    result[key] = sum(value) / len(value)
my_dict = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
for key in my_dict:
    if my_dict[key] < 4.50:
        result.pop(key)

    else:
        print(f"{key} -> {my_dict[key]:.2f}")
