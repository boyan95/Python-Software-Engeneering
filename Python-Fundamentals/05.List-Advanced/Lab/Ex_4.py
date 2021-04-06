nums = [int(el) for el in input().split(", ")]


even_numbers = [el for el in range(len(nums)) if nums[el] % 2 == 0]
                                            # това е са индексите от nums
print(even_numbers)


"""
прехвърляне на стрингове към инт НАЧИНИ:
nums_as_strings = ["1", "2", "3", "4"]

def converted_to_int(el):
    return int(el)

1. numbers = [int(el) for el in nums_as_strings]
2. numbers = [converted_to_int(el) for el in nums_as_strings] използва се функцията от по-горе
3. numbers = [list(map(int, nums_as_strings))] мапни ми всеки един елемент от nums_as_strings към int и после го превърни в лист
4. numbers = [list(map(lambda el: int(el), nums_as_strings))] това се използва много рядко
5. numbers = [list(map(lambda el: converted_to_int(el), nums_as_strings))]

филтриране на четните числа от лист
nums = [1, 2, 3, 4]

1. evens =[el for el in nums if el % 2 == 0]

или

2. evens = [list(filter(lambda el: el % 2 == 0, nums))]
"""