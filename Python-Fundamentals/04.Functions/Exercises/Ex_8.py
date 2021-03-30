input_number = int(input())


def loading_bar(current_number):
    a = "%"
    b = "."

    if current_number < 100:
        print(f"{current_number}% [{(current_number // 10) * a}{(10 - current_number//10) * b}]")
        print("Still loading...")
    else:
        print(f"{current_number}% Complete!")
        print(f"[{(current_number // 10) * a}]")


loading_bar(input_number)
