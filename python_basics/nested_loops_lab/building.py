top_floor = int(input())
prop_per_floor = int(input())

max_floor = top_floor
prop = 0

for floor in range(top_floor, 0, -1):
    prefix = 'A'
    if floor % 2 == 0:
        prefix = 'O'
    if floor == max_floor:
        prefix = 'L'

    for prop in range(0, prop_per_floor):
        print(f'{prefix}{floor}{prop}', end=' ')
    print()
