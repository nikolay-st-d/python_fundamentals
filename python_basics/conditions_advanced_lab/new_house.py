flower = input()  # "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
flowers_pcs = int(input())
budget = int(input())
price = 0
disc_mult = 1

if flower == 'Roses':
    price = 5
    if flowers_pcs > 80:
        disc_mult = 0.9
elif flower == 'Dahlias':
    price = 3.8
    if flowers_pcs > 90:
        disc_mult = 0.85
elif flower == 'Tulips':
    price = 2.8
    if flowers_pcs > 80:
        disc_mult = 0.85
elif flower == 'Narcissus':
    price = 3
    if flowers_pcs < 120:
        disc_mult = 1.15
elif flower == 'Gladiolus':
    price = 2.5
    if flowers_pcs < 80:
        disc_mult = 1.20

sub_total = flowers_pcs * price
total_price = sub_total * disc_mult
diff = budget - total_price

if diff >= 0:
    print(f"Hey, you have a great garden with {flowers_pcs} {flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(diff):.2f} leva more.")
