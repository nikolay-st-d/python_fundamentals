exc_price = float(input())
puzzle = int(input())
puppy = int(input())
bear = int(input())
mignon = int(input())
track = int(input())
puzzles_total = puzzle * 2.60
puppies_total = puppy * 3.00
bears_total = bear * 4.10
mignons_total = mignon * 8.20
tracks_total = track * 2.00
pcs_total = puzzle + puppy + bear + mignon + track
order_total = puzzles_total + puppies_total + bears_total + mignons_total + tracks_total
if pcs_total >= 50:
    discount = order_total * 0.25
    order_total = order_total - discount
rent = order_total * 0.1
order_total = order_total - rent
if exc_price <= order_total:
    money_left = order_total - exc_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = exc_price - order_total
    print(f"Not enough money! {money_left:.2f} lv needed.")
