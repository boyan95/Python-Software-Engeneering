data = input()
letter = []
digits = []
others = []

for el in data:
    if el.isalpha():
        letter.append(el)
    elif el.isdigit():
        digits.append(el)
    else:
        others.append(el)

print(f"{''.join(digits)}\n{''.join(letter)}\n{''.join(others)}")
