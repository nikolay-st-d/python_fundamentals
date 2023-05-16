x = float(input())
y = float(input())
h = float(input())

surface_green = x * x * 2 - 1.2 * 2
surface_green += x * y * 2 - 1.5 * 1.5 * 2
green_lt = surface_green / 3.4
surface_red = x * y * 2
surface_red += (x * h / 2) * 2
red_lt = surface_red / 4.3

print(f'{green_lt:.2f}')
print(f'{red_lt:.2f}')
