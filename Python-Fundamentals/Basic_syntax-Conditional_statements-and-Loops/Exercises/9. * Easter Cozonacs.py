budget = float(input())
flour_price = float(input())

colored_eggs = 0
counter_cozonac = 0

milk_price = (flour_price * 1.25) / 4
eggs_price = flour_price * 0.75

cozonac = flour_price + milk_price + eggs_price

while budget >= 0 and not budget < cozonac:
    budget -= cozonac
    counter_cozonac += 1
    colored_eggs += 3
    if counter_cozonac % 3 == 0:
        colored_eggs = colored_eggs - (counter_cozonac -2)

print(f"You made {counter_cozonac} cozonacs! Now you have { colored_eggs} eggs and {budget:.2f}BGN left.")
