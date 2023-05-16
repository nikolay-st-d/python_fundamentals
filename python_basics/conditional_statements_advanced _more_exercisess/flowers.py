chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

bouquet_price = 0

if season == 'Spring' or season == 'Summer':
    bouquet_price = chrysanthemums * 2 + roses * 4.1 + tulips * 2.5
    if holiday == 'Y':
        bouquet_price *= 1.15
    if tulips > 7 and season == 'Spring':
        bouquet_price *= 0.95
elif season == 'Autumn' or season == 'Winter':
    bouquet_price = chrysanthemums * 3.75 + roses * 4.5 + tulips * 4.15
    if holiday == 'Y':
        bouquet_price *= 1.15
    if roses >= 10 and season == 'Winter':
        bouquet_price *= 0.9

if chrysanthemums + roses + tulips > 20:
    bouquet_price *= 0.8

print(f'{bouquet_price + 2:.2f}')
