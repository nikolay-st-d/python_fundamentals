temp = int(input())
time = input()

clothing = ''
shoes = ''

if 10 <= temp <= 18:
    if time == 'Morning':
        clothing = 'Sweatshirt'
        shoes = 'Sneakers'
    elif time == 'Afternoon':
        clothing = 'Shirt'
        shoes = 'Moccasins'
    elif time == 'Evening':
        clothing = 'Shirt'
        shoes = 'Moccasins'
elif 18 < temp <= 24:
    if time == 'Morning':
        clothing = 'Shirt'
        shoes = 'Moccasins'
    elif time == 'Afternoon':
        clothing = 'T-Shirt'
        shoes = 'Sandals'
    elif time == 'Evening':
        clothing = 'Shirt'
        shoes = 'Moccasins'
elif temp >= 25:
    if time == 'Morning':
        clothing = 'T-Shirt'
        shoes = 'Sandals'
    elif time == 'Afternoon':
        clothing = 'Swim Suit'
        shoes = 'Barefoot'
    elif time == 'Evening':
        clothing = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {temp} degrees, get your {clothing} and {shoes}.")