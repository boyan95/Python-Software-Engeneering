positions_in_alphabet = {chr(ele + 97): ele + 1 for ele in range(26)}

data = input().split()
total = 0
for el in data:
    first_letter = el[0]
    last_letter = el[-1]
    nums = int(el[1:-1])

    if first_letter.isupper():
        nums /= positions_in_alphabet[first_letter.lower()]
    elif first_letter.islower():
        nums *= positions_in_alphabet[first_letter]

    if last_letter.isupper():
        nums -= positions_in_alphabet[last_letter.lower()]
    elif last_letter.lower():
        nums += positions_in_alphabet[last_letter]

    total += nums
print(f"{total:.2f}")
