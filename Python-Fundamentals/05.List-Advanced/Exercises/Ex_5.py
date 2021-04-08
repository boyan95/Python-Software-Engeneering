numbers_of_electron = int(input())
electrons = []
cell_number = 1
while numbers_of_electron > 0:
    possible_electrons = 2 * cell_number ** 2
    if possible_electrons > numbers_of_electron:
        electrons.append(numbers_of_electron)
    else:
        electrons.append(possible_electrons)
    numbers_of_electron -= possible_electrons
    cell_number += 1
print(electrons)
