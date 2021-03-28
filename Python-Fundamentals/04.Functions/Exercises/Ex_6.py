input_text = list(input())


def login(password):
    counter = 0
    is_valid = True
    if not (6 <= len(password) <= 10):
        is_valid = False
        print("Password must be between 6 and 10 characters")
    for el in password:
        if not el.isalnum():
            is_valid = False
            print("Password must consist only of letters and digits")
            break
    for el in password:
        if el.isnumeric():
            counter += 1
    if counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")


login(input_text)
