budget = float(input())
season = input()
location = ''
host_type = ''
price = 0

if budget <= 1000:
    host_type = 'Camp'
    if season == 'Summer':
        price = budget * 0.65
    elif season == 'Winter':
        price = budget * 0.45
elif 1000 < budget <= 3000:
    host_type = 'Hut'
    if season == 'Summer':
        price = budget * 0.80
    elif season == 'Winter':
        price = budget * 0.60
else:
    host_type = 'Hotel'
    price = budget * 0.9

if season == 'Summer':
    location = 'Alaska'
else:
    location = 'Morocco'

print(f'{location} - {host_type} - {price:.2f}')
