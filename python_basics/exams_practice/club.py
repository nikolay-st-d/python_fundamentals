profit_needed = float(input())
profit = 0


while profit < profit_needed:
    coctail = input()

    if coctail == 'Party!':
        print(f'We need {profit_needed - profit:.2f} leva more.')
        break

    coctail_number = int(input())

    price = len(coctail) * coctail_number
    if price % 2 != 0:
        price *= 0.75

    profit += price

if profit >= profit_needed:
    print(f'Target acquired.')
print(f'Club income - {profit:.2f} leva.')
