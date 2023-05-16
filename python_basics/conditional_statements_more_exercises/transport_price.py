trip_km = int(input())
day_night = input()
trip_price = 0

if trip_km < 20:
    if day_night == 'day':
        trip_price = trip_km * 0.79 + 0.70
    elif day_night == 'night':
        trip_price = trip_km * 0.90 + 0.70
elif 100 > trip_km >= 20:
    trip_price = trip_km * 0.09
elif trip_km >= 100:
    trip_price = trip_km * 0.06

print(f'{trip_price:.2f}')