money = float(input())  # 1.00 - 1 000 000.00
final_year = int(input())  # 1801 - 1900

curr_age = 18

for i in range(1800, final_year + 1):
    if i % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * curr_age
    curr_age += 1
if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    print(f'He will need {abs(money):.2f} dollars to survive.')
