number_of_orders = int(input())
total_for_all_orders = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())  # 0.01-100.00
    days = int(input())  # 1-31
    capsules_per_day = int(input())  # 1-2000

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        price_for_order = price_per_capsule * days * capsules_per_day
        total_for_all_orders += price_for_order
        print(f'The price for the coffee is: ${price_for_order:.2f}')
    else:
        continue
print(f'Total: ${total_for_all_orders:.2f}')

