materials = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False
legendary_item = ''

while True:
    input_data = input().split()
    for i in range(0, len(input_data), 2):
        material = input_data[i + 1].lower()
        quantity = int(input_data[i])
        if material not in materials:
            materials[material] = quantity
        else:
            materials[material] += quantity
        if materials['shards'] >= 250:
            legendary_item = 'Shadowmourne'
            materials['shards'] -= 250
            obtained = True
            break
        elif materials['fragments'] >= 250:
            legendary_item = 'Valanyr'
            materials['fragments'] -= 250
            obtained = True
            break
        elif materials['motes'] >= 250:
            legendary_item = 'Dragonwrath'
            materials['motes'] -= 250
            obtained = True
            break
    if obtained:
        break
print(f'{legendary_item} obtained!')
for key, value in materials.items():
    print(f'{key}: {value}')