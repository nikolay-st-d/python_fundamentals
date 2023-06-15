energy = int(input())
count_of_won_battles = 0
command = input()

while command != 'End of battle':
    distance = int(command)

    if energy >= distance and energy > 0:
        energy -= distance
        count_of_won_battles += 1

        if count_of_won_battles % 3 == 0:
            energy += count_of_won_battles
    else:
        print(f'Not enough energy! Game ends with {count_of_won_battles} won battles and {energy} energy')
        break

    command = input()
else:
    print(f'Won battles: {count_of_won_battles}. Energy left: {energy}')

