data = input().split()
command = input()

while not command == "END":

    if command == "Change":
        painting_number, changed_number = command.split()
    elif command == "Hide":
        painting_number = command.split()
    elif command == "Switch":
        painting_number, painting_number_2 = command.split()
    elif "Insert" in command:
        typ, place, painting_number = command.split()
        data.insert(place + 1, painting_number)
    elif command == "Reverse":
        data = data[::-1]
    command = input()
print(data)
