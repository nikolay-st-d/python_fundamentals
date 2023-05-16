fuel_type = input()
fuel_qty = float(input())
club_card = input()

total_price = 0

gasoline_price = 2.22
gas_price = 0.93
diesel_price = 2.33

if club_card == 'Yes':
    gasoline_price -= 0.18
    gas_price -= 0.08
    diesel_price -= 0.12

if fuel_type == 'Gasoline':
    total_price = fuel_qty * gasoline_price
elif fuel_type == 'Gas':
    total_price = fuel_qty * gas_price
elif fuel_type == 'Diesel':
    total_price = fuel_qty * diesel_price

if 20 <= fuel_qty <= 25:
    total_price *= 0.92
elif fuel_qty > 25:
    total_price *= 0.9

print(f'{total_price:.2f} lv.')
