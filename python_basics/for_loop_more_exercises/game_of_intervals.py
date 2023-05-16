moves = int(input())

points = 0
num_9 = 0
num_19 = 0
num_29 = 0
num_39 = 0
num_50 = 0
num_0 = 0

for i in range(moves):
    num = int(input())
    if 0 <= num <= 9:
        points += num * 0.2
        num_9 += 1
    elif 10 <= num <= 19:
        points += num * 0.3
        num_19 += 1
    elif 20 <= num <= 29:
        points += num * 0.4
        num_29 += 1
    elif 30 <= num <= 39:
        points += 50
        num_39 += 1
    elif 40 <= num <= 50:
        points += 100
        num_50 += 1
    elif num < 0 or num > 50:
        points /= 2
        num_0 += 1

print(f'{points:.2f}')
print(f'From 0 to 9: {num_9 / moves * 100:.2f}%')
print(f'From 10 to 19: {num_19 / moves * 100:.2f}%')
print(f'From 20 to 29: {num_29 / moves * 100:.2f}%')
print(f'From 30 to 39: {num_39 / moves * 100:.2f}%')
print(f'From 40 to 50: {num_50 / moves * 100:.2f}%')
print(f'Invalid numbers: {num_0 / moves * 100:.2f}%')