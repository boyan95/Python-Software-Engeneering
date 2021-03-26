chr_one = input()
chr_two = input()
res = []


def chars_in_range():
    for chr_to_number in range(ord(chr_one) + 1, ord(chr_two)):
        res.append(chr_to_number)
        for number_to_char in res:
            number_to_char = int(number_to_char)
            solve = chr(number_to_char)
        print(solve, end=" ")


chars_in_range()
