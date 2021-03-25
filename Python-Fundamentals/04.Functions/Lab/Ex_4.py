input_product = input()
input_quantity = int(input())


def total_price(product, quantity):
    result = 0
    if product == "coffee":
        result = 1.50 * quantity
    elif product == "water":
        result = 1.00 * quantity
    elif product == "coke":
        result = 1.40 * quantity
    elif product == "snacks":
        result = 2.00 * quantity
    return result


print(f"{total_price(input_product, input_quantity):.2f}")
