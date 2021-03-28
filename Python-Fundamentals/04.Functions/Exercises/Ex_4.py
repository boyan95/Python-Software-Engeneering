number = int(input())
number_to_str = str(number)


def odd_and_even_sum():
    odd = 0
    even = 0
    for num in number_to_str:
        num = int(num)
        if num == 0:
            continue
        elif num % 2 == 0:
            even += num
        elif num % 2 == 1:
            odd += num
    print(f"Odd sum = {odd}, Even sum = {even}")


odd_and_even_sum()
