first_number = int(input())
second_number = int(input())
third_number = int(input())


def add_and_subtract(a, b, c):
    def add_res():
        return a + b

    def subtract_res():
        return -c

    return add_res() + subtract_res()


print(add_and_subtract(first_number, second_number, third_number))
