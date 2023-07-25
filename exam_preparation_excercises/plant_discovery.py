def rate(plants_dict, some_plant, some_rating):
    plants_dict[some_plant]['ratings'].append(int(some_rating))
    return plants_dict


def update(plants_dict, some_plant, some_rating):
    plants[some_plant]['rarity'] = some_rating
    return plants_dict


def reset(plants_dict, some_plant):
        plants[some_plant]['ratings'] = []
        return plants_dict


number_of_rows = int(input())
plants = {}
for _ in range(number_of_rows):
    plant_name, rarity = input().split('<->')
    rarity = int(rarity)
    plants[plant_name] = {'rarity': rarity, 'ratings': []}

command = input()
while command != 'Exhibition':
    actions = command.split(' ')
    if actions[0] == 'Rate:':
        plant = actions[1]
        rating = actions[3]
        if plant in plants.keys():
            plants = rate(plants, plant, rating)
        else:
            print('error')
    elif actions[0] == 'Update:':
        plant = actions[1]
        new_rating = actions[3]
        if plant in plants.keys():
            plants = update(plants, plant, new_rating)
        else:
            print('error')
    elif actions[0] == 'Reset:':
        plant = actions[1]
        if plant in plants.keys():
            plants = reset(plants, plant)
        else:
            print('error')
    command = input()

print('Plants for the exhibition:')
for key, value in plants.items():
    rarity, ratings_list = value.values()
    average_rating = 0
    if ratings_list:
        average_rating = sum(ratings_list) / len(ratings_list)
    print(f'- {key}; Rarity: {rarity}; Rating: {average_rating:.2f}')
