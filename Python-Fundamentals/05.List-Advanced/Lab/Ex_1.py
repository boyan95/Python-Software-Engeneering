count_wagons = int(input())
command = input()


train = [0 for _ in range(count_wagons)]


while not command == "End":
    if command.split()[0] == "add":
        train[-1] += int(command.split()[1])
    if command.split()[0] == "insert":
        train[int(int(command.split()[1]))] += int(command.split()[2])
    if command.split()[0] == "leave":
        train[int(command.split()[1])] -= int(command.split()[2])
    command = input()

print(train)
