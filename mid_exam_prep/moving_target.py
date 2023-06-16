def shoot(targets_list, element_index, power):
    if element_index in range(len(targets_list)):
        if targets_list[element_index] > power:
            targets_list[element_index] -= power
        else:
            targets_list.pop(element_index)
    return targets_list


def add(targets_list, element_index, value):
    if element_index in range(len(targets_list)):
        targets_list.insert(element_index, value)
    else:
        print('Invalid placement!')
    return targets_list


def strike(targets_list, element_index, radius):
    border_index_1 = element_index - radius
    border_index_2 = element_index + radius + 1
    if border_index_1 in range(len(targets_list)) and border_index_2 in range(len(targets_list)):
        targets_list = targets_list[:border_index_1] + targets_list[border_index_2:]
    else:
        print('Strike missed!')
    return targets_list


targets = [int(x) for x in input().split()]

input_data = input()

while input_data != 'End':

    command_list = input_data.split()
    command, index, data = command_list[0], int(command_list[1]), int(command_list[2])

    if command == 'Shoot':
        targets = shoot(targets, index, data)
    elif command == 'Add':
        targets = add(targets, index, data)
    elif command == 'Strike':
        targets = strike(targets, index, data)

    input_data = input()

print(*targets, sep='|')

