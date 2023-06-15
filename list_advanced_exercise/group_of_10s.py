numbers_list = list(map(int, input().split(', ')))
current_group = 10
while numbers_list:
    group_list = [num for num in numbers_list if num <= current_group]
    print(f"Group of {current_group}'s: {group_list}")
    numbers_list = [num for num in numbers_list if num not in group_list]
    current_group += 10

