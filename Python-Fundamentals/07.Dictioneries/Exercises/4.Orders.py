command = input()
orders = {}

while not command == "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in orders:
        orders[product] = [price]
        orders[product].append(quantity)
    else:
        if not price == orders[product][0]:
            orders[product][0] = price
            orders[product][1] += quantity
        else:
            orders[product][1] += quantity
    command = input()
for product, digits in orders.items():
    print(f"{product} -> {(digits[0]* digits[1]):.2f}")



