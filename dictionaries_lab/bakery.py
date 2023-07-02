all_stuff = input().split()
new_dict = {}

for item in range(0, len(all_stuff), 2):
    key = all_stuff[item]
    value = int(all_stuff[item + 1])
    new_dict[key] = value

print(new_dict)