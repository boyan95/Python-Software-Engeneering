data = list(input())
current_el = 0
result = ""

for el in data:
    if current_el+1 == len(data):
        result += el
        break
    if data[current_el] == data[current_el + 1]:
        el = el.replace(el, "")
    else:
        result += el
    current_el += 1
print(result)
