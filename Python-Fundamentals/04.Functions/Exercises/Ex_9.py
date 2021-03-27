num_one = int(input())
num_two = int(input())


def factorial_division(n):
    res = 1
    for num in range(1, n + 1):
        res *= num
    return res


factorial_number_1 = factorial_division(num_one)
factorial_number_2 = factorial_division(num_two)

result = factorial_number_1 / factorial_number_2

print(f"{result:.2f}")
