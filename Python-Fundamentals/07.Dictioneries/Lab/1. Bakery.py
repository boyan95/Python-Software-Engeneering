elements = input().split()

products = {}
for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    products[key] = value

print(products)