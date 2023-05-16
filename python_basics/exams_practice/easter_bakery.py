flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_lots = int(input())
east_packages = int(input())

flour_total = flour_kg * flour_price
sugar_total = sugar_kg * flour_price * 0.75
eggs_total = egg_lots * flour_price * 1.1
east_total = east_packages * flour_price * 0.75 * 0.2

total = flour_total + sugar_total + eggs_total + east_total

print(f'{total:.2f}')