items = input().split("|")
budget = float(input())

profit = 0
overall_profit = 0
sum = 0
list_of_items = []

for item in items:
    typ, price = item.split("->")
    price = float(price)
    if typ == "Clothes" and price > 50:
        continue
    elif typ == "Shoes" and price > 35:
        continue
    elif typ == "Accessories" and price > 20.50:
        continue

    if budget >= price:
        budget -= price
        profit = price * 1.4
        sum += profit
        overall_profit += price * 0.4
        list_of_items.append(profit)
        profit = 0

for el in list_of_items:
    print(f"{el:.2f}", end=" ")

print()
print(f"Profit: {overall_profit:.2f}")
if sum + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
