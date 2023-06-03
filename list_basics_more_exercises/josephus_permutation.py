people_list_str = input().split()
people_list = []
for element in people_list_str:
    people_list.append(int(element))
step = int(input())
executed = []
current_index = step - 1

while len(people_list) > 0:
    if step > len(people_list):
        step -= len(people_list)
        current_index = step - 1
    executed.append(people_list[current_index])
    people_list.pop(current_index)
    current_index += step - 1
print(people_list)
print(executed)

