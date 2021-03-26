first_number = int(input())
second_number = int(input())
third_number = int(input())


def the_smallest_number(a, b, c):
    if a < b and a < c:
        min_number = first_number
    elif b < a and b < c:
        min_number = second_number
    elif c < a and c < b:
        min_number = third_number
    return min_number


print(the_smallest_number(first_number, second_number, third_number))
