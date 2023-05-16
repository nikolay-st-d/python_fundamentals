from math import floor

tours = int(input())
start_points = int(input())

points = start_points
wins = 0

for _ in range(tours):
    rang = input()
    if rang == 'W':
        wins += 1
        points += 2000
    elif rang == 'F':
        points += 1200
    elif rang == 'SF':
        points += 720

print(f'Final points: {points}')
print(f'Average points: {floor((points - start_points) / tours)}')
print(f'{wins / tours * 100:.2f}%')

