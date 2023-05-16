width = int(input())
length = int(input())
height = int(input())

space_left = width * length * height

while True:
    com = input()

    if com == 'Done':
        print(f'{space_left} Cubic meters left.')
        break
    else:
        boxes = int(com)
        space_left -= boxes

        if space_left < 1:
            print(f'No more free space! You need {abs(space_left)} Cubic meters more.')
            break
