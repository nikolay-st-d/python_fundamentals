from math import ceil

h = int(input())
w = int(input())
ex_perc = int(input())

surface = h * w * 4
all_surface = ceil(surface - (surface * ex_perc) / 100)

surface_left = all_surface
all_paint = 0

while surface_left > 0:
    com = input()

    if com == 'Tired!':
        print(f'{surface_left} quadratic m left.')
        break

    paint = int(com)
    surface_left -= paint
    all_paint += paint

if all_surface == all_paint:
    print('All walls are painted! Great job, Pesho!')
elif all_surface < all_paint:
    print(f'All walls are painted and you have {all_paint - all_surface} l paint left!')
