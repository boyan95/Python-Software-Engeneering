n = int(input())
positive_nums = []
negative_nums = []
count_of_positive_numbers = 0

for num in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_nums.append(current_number)
        count_of_positive_numbers +=1
    else:
        negative_nums.append(current_number)

print(positive_nums)
print(negative_nums)
print(f"Count of positives: {count_of_positive_numbers}. Sum of negatives: {sum(negative_nums)}")