number = int(input())


def perfect_number(n):
    count = 0
    for current_num in range(1, n):
        while number % current_num == 0:
            count += current_num
            break
    if count == n:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(number)
