vegetable_price = float(input())
fruit_price = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

income_eur = (vegetable_price * vegetable_kg + fruit_price * fruit_kg) / 1.94

print(f'{income_eur:.2f}')
