panetones = int(input())
egg_lots = int(input())
cookies = int(input())

total = panetones * 3.2
total += egg_lots * 4.35
total += cookies * 5.40
total += egg_lots * 12 * 0.15

print(f'{total:.2f}')

