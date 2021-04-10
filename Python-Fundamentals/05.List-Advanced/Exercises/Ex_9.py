days = int(input())
budget = float(input())
count_of_people = int(input())
fuel_price_per_kilometer = float(input())
food_price = float(input())
night_price = float(input())

costs_for_food = count_of_people * food_price
costs_per_night = count_of_people * night_price
if count_of_people > 10:
    costs_per_night *= 0.75
total = (costs_for_food + costs_per_night) * days

for current_day in range(1, days + 1):
    current_kilometers = float(input())
    costs_for_fuel = current_kilometers * fuel_price_per_kilometer
    total += costs_for_fuel

    if current_day % 3 == 0:
        total *= 1.4
    if current_day % 5 == 0:
        total *= 1.4
    if current_day % 7 == 0:
        total -= (total / count_of_people)
    if budget < total:
        print(f"Not enough money to continue the trip. You need {(total - budget):.2f}$ more.")
        break

if not budget < total:
    print(f"You have reached the destination. You have {(budget - total):.2f}$ budget left.")
