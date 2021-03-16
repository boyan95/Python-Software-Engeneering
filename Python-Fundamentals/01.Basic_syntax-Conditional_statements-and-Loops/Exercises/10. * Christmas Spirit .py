quantity = int(input())
days = int(input())

spirit = 0
costs = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        spirit += 5
        costs += ornament_set * quantity
    if day % 3 == 0:
        spirit += 13
        costs += ((tree_skirt + tree_garlands) * quantity)
    if day % 5 == 0:
        spirit += 17
        costs += tree_lights * quantity
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        costs += tree_skirt + tree_garlands + tree_lights
        if day == days:
            spirit -= 30

print(f"Total cost: {costs}")
print(f"Total spirit: {spirit}")
