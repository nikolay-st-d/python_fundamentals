guests = int(input())
couvert = float(input())
budget = float(input())

price = guests * couvert

if 10 <= guests <= 15:
    price *= 0.85
if 15 < guests <= 20:
    price *= 0.8
if guests > 20:
    price *= 0.75

cake = budget * 0.1  # cake

total = price + cake

if total <= budget:
    print(f'It is party time! {budget - total:.2f} leva left.')
else:
    print(f'No party! {total - budget:.2f} leva needed.')