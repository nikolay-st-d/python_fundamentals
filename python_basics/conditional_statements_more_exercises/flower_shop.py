from math import floor, ceil

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
present_price = float(input())

profit = (magnolias * 3.25 + hyacinths * 4 + roses * 3.50 + cacti * 8) * 0.95
diff = abs(profit - present_price)

if profit >= present_price:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')
