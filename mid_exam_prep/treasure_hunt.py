def loot(chest_list, loots):
    for item in loots:
        if item not in chest_list:
            chest_list.insert(0, item)
    return chest_list


def drop(chest_list, index):
    if index in range(len(chest_list)):
        chest_list.append(chest_list.pop(index))
    return chest_list


def steal(chest_list, count):
    if len(chest_list) >= count:
        border_index = len(chest_list) - count
        print(', '.join(chest_list[border_index:]))
        chest_list = chest_list[:border_index]
    else:
        print(', '.join(chest_list))
        chest_list = []
    return chest_list


chest = input().split('|')
input_data = input()

while input_data != 'Yohoho!':

    data_list = input_data.split()
    command = data_list[0]

    if command == 'Loot':
        loot_list = data_list[1:]
        chest = loot(chest, loot_list)
    elif command == 'Drop':
        loot_index = int(data_list[1])
        chest = drop(chest, loot_index)
    elif command == 'Steal':
        loots_count = int(data_list[1])
        chest = steal(chest, loots_count)

    input_data = input()

if chest:
    average_gain = sum([len(x) for x in chest]) / len(chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")