number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:
    commands = input().split(' ')
    if commands[0] == 'End':
        print(train)
        break
    if commands[0] == 'add':
        train[ -1] += int(commands[1])
    elif commands[0] == 'insert':
        wagon = int(commands[1])
        train[wagon] += int(commands[2])
    elif commands[0] == 'leave':
        wagon = int(commands[1])
        train[wagon] -= int(commands[2])


