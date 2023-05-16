from math import floor

balls = int(input())

total_points = 0
reds = 0
oranges = 0
yellows = 0
whites = 0
blacks = 0
others = 0
divides = 0

for i in range(balls):
    color = input()

    if color == 'red':
        total_points += 5
        reds += 1
    elif color == 'orange':
        total_points += 10
        oranges += 1
    elif color == 'yellow':
        total_points += 15
        yellows += 1
    elif color == 'white':
        total_points += 20
        whites += 1
    elif color == 'black':
        total_points = floor(total_points / 2)
        divides += 1
        blacks += 1
    else:
        others += 1
        continue

print(f"Total points: {total_points}")
print(f"Red balls: {reds}")
print(f"Orange balls: {oranges}")
print(f"Yellow balls: {yellows}")
print(f"White balls: {whites}")
print(f"Other colors picked: {others}")
print(f"Divides from black balls: {divides}")