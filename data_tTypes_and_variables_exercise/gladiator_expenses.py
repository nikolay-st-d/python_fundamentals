lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_count = 0
sword_count = 0
shield_count = 0
armor_count = 0

for game in range(1, lost_fights_count + 1):
    helmet_brake = False
    sword_brake = False
    if game % 2 == 0:
        helmet_count += 1
        helmet_brake = True
    if game % 3 == 0:
        sword_count += 1
        sword_brake = True
    if helmet_brake and sword_brake:
        shield_count += 1
        if shield_count % 2 == 0:
            armor_count += 1

all_expenses = helmet_count * helmet_price + sword_count * sword_price + shield_count * shield_price + armor_count * armor_price
print(f"Gladiator expenses: {all_expenses:.2f} aureus")
