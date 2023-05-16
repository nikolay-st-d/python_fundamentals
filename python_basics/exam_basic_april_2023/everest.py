days = 1
level = 5364

while True:

    command = input()

    if command == 'Yes':
        days += 1

    if command == 'END' or days > 5:
        break

    climbed = int(input())

    level += climbed

    if level >= 8848:
        print(f'Goal reached for {days} days!')
        break


if level < 8848:
    print('Failed!')
    print(f'{level}')