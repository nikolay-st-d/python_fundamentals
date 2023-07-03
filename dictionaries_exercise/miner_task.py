data_list = []
data_dict = {}
while True:
    data = input()
    if data == 'stop':
        break
    data_list.append(data)

for i in range(0, len(data_list), 2):
    key = data_list[i]
    value = int(data_list[i + 1])
    if key not in data_dict.keys():
        data_dict[key] = value
    else:
        data_dict[key] += value

for key, value in data_dict.items():
    print(f"{key} -> {value}")