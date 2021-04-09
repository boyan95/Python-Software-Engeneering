nums_to_int = [int(el) for el in input().split(", ")]
sorted_nums = sorted(nums_to_int)
result = []
max_num = sorted_nums[-1] // 10

for j in range(1, max_num + 1):
    result.append([])
if sorted_nums[-1] / 10 > max_num:
    result.append([])
for index in range(0, max_num):
    for i in nums_to_int:
        while i // 10 == index:
            if i // 10 == max_num:
                result[-1].append(i)
            result[index].append(i)
            break
if i // 10 == max_num:
    result[-1].append(i)

counter = 10
for k in range(0, len(result)):
    print(f"Group of {((k + 10) // 10) * counter}'s: {result[k]}")
    counter += 10
