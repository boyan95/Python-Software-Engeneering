nums = int(input())

even_nums = []
odd_nums = []
positive_nums = []
negative_nums = []

for i in range(nums):
    current_num = int(input())
    if current_num % 2 == 0:
        even_nums.append(current_num)
    if not current_num % 2 == 0:
        odd_nums.append(current_num)
    if current_num >= 0:
        positive_nums.append(current_num)
    if current_num < 0:
        negative_nums.append(current_num)

command = input()
if command == "even":
    print(even_nums)
elif command == "odd":
    print(odd_nums)
elif command == "negative":
    print(negative_nums)
elif command == "positive":
    print(positive_nums)