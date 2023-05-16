from math import ceil

guests = int(input())
budget = int(input())

east_breads = ceil(guests / 3)
eggs = guests * 2

total = east_breads * 4 + eggs * 0.45

if budget >= total:
    print(f'Lyubo bought {east_breads} Easter bread and {eggs} eggs.')
    print(f'He has {budget - total:.2f} lv. left.')
else:
    print(f"Lyubo doesn't have enough money.")
    print(f'He needs {total - budget:.2f} lv. more.')