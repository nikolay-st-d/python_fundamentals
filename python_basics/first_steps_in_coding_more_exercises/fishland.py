price_mackerel = float(input())
price_sprinkle = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussels_kg = float(input())

bonito_price = bonito_kg * price_mackerel * 1.6
scad_price = scad_kg * price_sprinkle * 1.8
mussels_price = mussels_kg * 7.5
total = bonito_price + scad_price + mussels_price

print(f'{total:.2f}')
