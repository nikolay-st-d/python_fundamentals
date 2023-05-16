groups_n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(groups_n):
    people_in_group = int(input())
    if people_in_group <= 5:
        p1 += people_in_group
    elif 6 <= people_in_group <= 12:
        p2 += people_in_group
    elif 13 <= people_in_group <= 25:
        p3 += people_in_group
    elif 26 <= people_in_group <= 40:
        p4 += people_in_group
    else:
        p5 += people_in_group

people_total = p1 + p2 + p3 + p4 + p5

print(f'{p1 / people_total * 100:.2f}%')
print(f'{p2 / people_total * 100:.2f}%')
print(f'{p3 / people_total * 100:.2f}%')
print(f'{p4 / people_total * 100:.2f}%')
print(f'{p5 / people_total * 100:.2f}%')

