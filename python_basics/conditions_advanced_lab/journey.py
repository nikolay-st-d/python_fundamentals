budget = float(input())
season = input()

destination = ''
host = ''

if budget <= 100:
    if season == 'summer':
        budget *= 0.3
        host = 'Camp'
    elif season == 'winter':
        budget *= 0.7
        host = 'Hotel'
    destination = 'Bulgaria'
elif 100 < budget <= 1000:
    if season == 'summer':
        budget *= 0.4
        host = 'Camp'
    elif season == 'winter':
        budget *= 0.8
        host = 'Hotel'
    destination = 'Balkans'
elif budget > 1000:
    budget *= 0.9
    destination = 'Europe'
    host = 'Hotel'

print(f"Somewhere in {destination}")  # "Bulgaria" or "Balkans" or "Europe"
print(f"{host} - {budget:.2f}")  # "Camp" or "Hotel"
