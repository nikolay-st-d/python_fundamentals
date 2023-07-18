import re

regex_1 = '[A-Za-z]+'
regex_2 = '[0-9]'
names = input().split(', ')
data = input()
results = {}
while data != 'end of race':
    match_name = re.findall(regex_1, data)
    match_distance = re.findall(regex_2, data)
    if match_name and match_distance:
        name = ''.join(match_name)
        distance = sum([int(x) for x in match_distance])
        if name in names:
            if name in results.keys():
                results[name] += distance
            else:
                results[name] = distance
    data = input()
sorted_results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}
winners = list(sorted_results.keys())
print(f'1st place: {winners[0]}')
print(f'2nd place: {winners[1]}')
print(f'3rd place: {winners[2]}')