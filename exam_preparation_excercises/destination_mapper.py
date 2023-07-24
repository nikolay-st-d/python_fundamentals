import re
destinations = []
travel_points = 0
data = input()
regex = r'([=\/]{1})([A-Z]{1}[A-Za-z]{2,})\1'
matches = re.findall(regex, data)
for match in matches:
    destinations.append(match[1])
    travel_points += len(match[1])

print(f"Destinations: {', '.join(destinations)}")
print(f'Travel Points: {travel_points}')