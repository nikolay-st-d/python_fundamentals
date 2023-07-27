cities = {}
primary_data = input()
while primary_data != 'Sail':
        city, people, gold = primary_data.split('||')
        people = int(people)
        gold = int(gold)
        if city in cities.keys():
            cities[city]['people'] += people
            cities[city]['gold'] += gold
        else:
            cities[city] = {'people': people, 'gold': gold}
        primary_data = input()
# print(cities)
command = input()
while command != 'End':
    data = command.split('=>')
    action = data[0]
    if action == 'Plunder':
        town = data[1]
        people = int(data[2])
        gold = int(data[3])
        cities[town]['people'] -= people
        cities[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]['people'] == 0 or cities[town]['gold'] == 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    if action == 'Prosper':
        town = data[1]
        gold = int(data[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    command = input()

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, value in cities.items():
        people = value['people']
        gold = value['gold']
        print(f'{key} -> Population: {people} citizens, Gold: {gold} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")