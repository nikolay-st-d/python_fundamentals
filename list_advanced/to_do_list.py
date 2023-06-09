tasks_list = []
while True:
    task = input()
    if task == 'End':
        break
    else:
        tasks_list.append(task)
sorted_list = sorted(tasks_list, key=lambda element: int(element.split('-')[0]))
final_list = [element.split('-')[1] for element in sorted_list]
print(final_list)
