command = input()
products = {}
while not command == "statistics":
    key, value = command.split(": ")
    value = int(value)
    if key in products:
        products[key] += int(value)
    else:
        products[key] = int(value)
    command = input()

print(f"Products in stock:")
for el in products:
    print(f"- {el}: {products.get(el)}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
