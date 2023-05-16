budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" или "Winter"
fishermen = int(input())

rent = 0
disc_mult = 1

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600
if fishermen <= 6:
    disc_mult = 0.9
elif 7 <= fishermen <= 11:
    disc_mult = 0.85
elif fishermen > 12:
    disc_mult = 0.75

price = rent * disc_mult

if fishermen % 2 == 0 and season != 'Autumn':
    price = price * 0.95

if budget - price >= 0:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
