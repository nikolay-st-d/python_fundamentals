fire_cells_list = input().split('#')
water = int(input())
total_effort = 0
total_fire = 0
processed_cells = []

for fire_cell in fire_cells_list:
    cell_is_valid = False
    fire_level, cell_value = fire_cell.split(' = ')
    cell_value = int(cell_value)

    if fire_level == 'High' and cell_value in range(81, 125 + 1):
        cell_is_valid = True
    elif fire_level == 'Medium' and cell_value in range(51, 80 + 1):
        cell_is_valid = True
    elif fire_level == 'Low' and cell_value in range(1, 50 + 1):
        cell_is_valid = True

    if cell_is_valid and water >= cell_value:
        water -= cell_value
        total_effort += cell_value * 0.25
        total_fire += cell_value
        processed_cells.append(cell_value)
print('Cells:')
for cell in processed_cells:
    print(f'- {cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
