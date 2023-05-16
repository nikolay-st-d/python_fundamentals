quantity_of_decorations = int(input())
days_left_to_chr = int(input())

money = 0
spirit = 0
current_day = 0

while days_left_to_chr > 0:
    current_day += 1

    if current_day % 11 == 0:
        quantity_of_decorations += 2

    if current_day % 2 == 0:
        money += 2 * quantity_of_decorations
        spirit += 5
    if current_day % 3 == 0:
        money += 8 * quantity_of_decorations
        spirit += 13
    if current_day % 5 == 0:
        money += 15 * quantity_of_decorations
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        money += 23

    if current_day % 10 == 0 and days_left_to_chr == 1:
        spirit -= 30

    days_left_to_chr -= 1

print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")
