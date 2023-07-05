data = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        side, user = command.split(' | ')
        if side not in data.keys() and user not in data.values():
            data[side] = [user]
        if user not in data.values():
            data[side].append(user)
    elif '->' in command:
        user, side = command.split(' -> ')
print(data)