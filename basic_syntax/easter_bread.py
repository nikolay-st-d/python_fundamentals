budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
bread_price = eggs_price + flour_price + milk_price / 4
current_bread_count = 0
colored_eggs_count = 0

while budget > bread_price:
    budget -= bread_price
    current_bread_count += 1
    colored_eggs_count += 3

    if current_bread_count % 3 == 0:
        colored_eggs_count -= current_bread_count - 2

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")

