happiness = input().split()
factor = int(input())
average_happiness = 0
counter = 0
multiplied_by_factor = [int(el) * factor for el in happiness]

for el in multiplied_by_factor:
    counter += 1
    average_happiness += el

total_happiness = [el for el in multiplied_by_factor if el >= average_happiness / counter]
if len(total_happiness) >= counter / 2:
    print(f"Score: {len(total_happiness)}/{counter}. Employees are happy!")
else:
    print(f"Score: {len(total_happiness)}/{counter}. Employees are not happy!")