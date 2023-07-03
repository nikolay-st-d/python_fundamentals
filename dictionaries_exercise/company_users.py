all_data = {}
data = input()
while data != 'End':
    course, id_number = data.split(' -> ')
    if course not in all_data:
        all_data[course] = [id_number]
    else:
        if id_number not in all_data[course]:
            all_data[course].append(id_number)
    data = input()

for course, id_number in all_data.items():
    print(course)
    for num in id_number:
        print(f'-- {num}')
