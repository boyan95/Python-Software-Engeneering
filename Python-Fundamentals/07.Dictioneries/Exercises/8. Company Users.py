command = input()
result = {}
while not command == "End":
    key, value = command.split(" -> ")
    if key in result and value in result[key]:
        command = input()
        continue
    elif key in result:
        result[key].append(value)
    else:
        result[key] = [value]
    command = input()
my_dict = dict(sorted(result.items(), key=lambda x: x[0]))
for key, value in my_dict.items():
    print(key)
    if len(value) > 1:
        m = '\n-- '.join(value)
        print(f"-- {m}")
    else:
        print(f"-- {' '.join(value)}")
