input_operation = input()
first_num = int(input())
second_num = int(input())


def solve(operation, a, b):
    result = 0
    if operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a // 2
    elif operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    return result


print(solve(input_operation, first_num, second_num))
