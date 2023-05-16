game_1 = input()
game_2 = input()
game_3 = input()

won = 0
lost = 0
drawn = 0

a, b = game_1.split(":")
if int(a) == int(b):
    drawn += 1
elif int(a) > int(b):
    won += 1
else:
    lost += 1

a, b = game_2.split(":")
if int(a) == int(b):
    drawn += 1
elif int(a) > int(b):
    won += 1
else:
    lost += 1

a, b = game_3.split(":")
if int(a) == int(b):
    drawn += 1
elif int(a) > int(b):
    won += 1
else:
    lost += 1

print(f'Team won {won} games.')
print(f'Team lost {lost} games.')
print(f'Drawn games: {drawn}')
