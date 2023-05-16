last_sector = input()
rows_first_sector = int(input())
places_odd_row = int(input())

places_count = 0
rows = rows_first_sector

for sector in range(ord('A'), ord(last_sector) + 1):
    rows += 1
    for row in range(1, rows):
        places = places_odd_row
        if row % 2 == 0:
            places = places_odd_row + 2
        for place in range(ord('a'), places + ord('a')):
            if place == places:
                break
            places_count += 1
            print(f'{chr(sector)}{row}{chr(place)}')
print(places_count)
