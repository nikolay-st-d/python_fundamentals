season = input()
odo_month = float(input())
salary = 0
payout_km = 0

if odo_month <= 5000:
    if season == 'Spring' or season =='Autumn':
        payout_km = 0.75
    elif season == 'Summer':
        payout_km = 0.9
    elif season == 'Winter':
        payout_km = 1.05
elif 5000 < odo_month <= 10000:
    if season == 'Spring' or season =='Autumn':
        payout_km = 0.95
    elif season == 'Summer':
        payout_km = 1.1
    elif season == 'Winter':
        payout_km = 1.25
elif 10000 < odo_month <= 20000:
    payout_km = 1.45

salary = odo_month * payout_km * 4 * 0.9

print(f'{salary:.2f}')
