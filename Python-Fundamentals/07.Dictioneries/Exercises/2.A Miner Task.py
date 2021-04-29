command = input()
as_list = []
result = {}
while not command == "stop":
    as_list.append(command)
    command = input()
while len(as_list) > 0:
    key = as_list[0]
    value = int(as_list[1])
    if key in result:
        result[key] += int(value)
        del as_list[0]
        del as_list[0]
        continue
    result[key] = value
    del as_list[0]
    del as_list[0]

for el in result:
    print(f"{el} -> {result.get(el)}")
