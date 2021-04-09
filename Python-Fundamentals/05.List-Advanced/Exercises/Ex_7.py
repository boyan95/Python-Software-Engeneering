code = input().split()
nums = []
letters = []

for el in code:
    for char in list(el):
        if char.isnumeric():
            nums.append(char)
        elif char.isalpha():
            letters.append(char)
    hole_number = "".join(nums)
    hole_number_as_int = int(hole_number)
    letters[0], letters[-1] = letters[-1], letters[0]
    letters.insert(0, chr(hole_number_as_int))
    x = "".join(letters)
    print(x, end=" ")
    nums.clear()
    letters.clear()


