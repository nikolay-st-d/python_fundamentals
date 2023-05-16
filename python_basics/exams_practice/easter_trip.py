destination = input()  # "France", "Italy", "Germany"
dates = input()  # "21-23", "24-27", "28-31"
nights = int(input())

price_night = 0

if destination == 'France':
    if dates == '21-23':
        price_night = 30
    elif dates == '24-27':
        price_night = 35
    elif dates == '28-31':
        price_night = 40
elif destination == 'Italy':
    if dates == '21-23':
        price_night = 28
    elif dates == '24-27':
        price_night = 32
    elif dates == '28-31':
        price_night = 39
elif destination == 'Germany':
    if dates == '21-23':
        price_night = 32
    elif dates == '24-27':
        price_night = 37
    elif dates == '28-31':
        price_night = 43

total = nights * price_night

print(f'Easter trip to {destination} : {total:.2f} leva.')