input_text = input().split(', ')


def palindrome_integers():
    for i in input_text:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


palindrome_integers()

# Str на обратно
# а = "Hello"
# print(a[::-1])
