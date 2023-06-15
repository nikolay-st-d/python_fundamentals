# 1

first_employee_efficiency_per_hour = int(input())
second_employee_efficiency_per_hour = int(input())
third_employee_efficiency_per_hour = int(input())
students_count = int(input())
hours_counter = 0
total_time = 0
total_efficiency_per_hour = first_employee_efficiency_per_hour + \
                            second_employee_efficiency_per_hour + \
                            third_employee_efficiency_per_hour
while students_count > 0:
    hours_counter += 1
    total_time += 1
    if hours_counter % 4 == 0:  # Break time
        continue
    students_count -= total_efficiency_per_hour
print(f"Time needed: {total_time}h.")


# 2

def loot(loots, list_of_items):
    for item in list_of_items:
        if item not in loots:
            loots.insert(0, item)
    return loots


def drop(loots, target_index):
    if target_index in range(len(loots)):  # index is valid
        removed_loot = loots.pop(target_index)
        loots.append(removed_loot)
    return loots


def steal(loots, count_of_steal):
    if count_of_steal >= len(loots):
        print(", ".join(loots))
        loots = []
    else:
        steal_index = len(loots) - count_of_steal
        print(", ".join(loots[steal_index:]))
        loots = loots[0:steal_index]
    return loots


initial_loot = input().split("|")
command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        items = command[1:]
        initial_loot = loot(initial_loot, items)
    elif action == "Drop":
        index = int(command[1])
        initial_loot = drop(initial_loot, index)
    elif action == "Steal":  # else
        count = int(command[1])
        initial_loot = steal(initial_loot, count)
    command = input()
if not initial_loot:  # if len(initial_loot)  == 0:
    print("Failed treasure hunt.")
else:
    average_gain = sum(len(item) for item in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")


# 3.1
def shoot(list_of_targets, target_index, shoot_power):
    if target_index in range(len(list_of_targets)):
        if list_of_targets[target_index] <= shoot_power:  # target is shoot
            list_of_targets.pop(target_index)
        else:  # target is not shoot, its value is greater than zero
            list_of_targets[target_index] -= shoot_power
    return list_of_targets


def add(list_of_targets, target_index, target_value):
    if target_index in range(len(list_of_targets)):  # index is valid
        list_of_targets.insert(target_index, target_value)
    else:  # index does not exist
        print("Invalid placement!")
    return list_of_targets


def strike(list_of_targets, target_index, radius):
    if target_index - radius in range(len(list_of_targets)) and \
            target_index + radius in range(len(list_of_targets)):  # index is valid
        list_of_targets = list_of_targets[0: target_index - radius] + \
                          list_of_targets[target_index + radius + 1:]
    else:  # some of edge indexes is not valid
        print("Strike missed!")
    return list_of_targets


targets = [int(target) for target in input().split()]
command = input()
while command != "End":
    command = command.split()
    action, index, value = command[0], int(command[1]), int(command[2])
    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)
    command = input()
print(*targets, sep="|")


# 3.2

def shoot(list_of_targets, target_index, shoot_power):
    if target_index in range(len(list_of_targets)):
        if list_of_targets[target_index] <= shoot_power:  # target is shoot
            list_of_targets.pop(target_index)
        else:  # target is not shoot, its value is greater than zero
            list_of_targets[target_index] -= shoot_power
    return list_of_targets


def add(list_of_targets, target_index, target_value):
    if target_index in range(len(list_of_targets)):  # index is valid
        list_of_targets.insert(target_index, target_value)
    else:  # index does not exist
        print("Invalid placement!")
    return list_of_targets


def strike(list_of_targets, target_index, radius):
    if target_index - radius in range(len(list_of_targets)) and \
            target_index + radius in range(len(list_of_targets)):  # index is valid
        removing_start_index = target_index - radius
        removing_final_index = target_index + radius
        for removing_index in range(removing_final_index, removing_start_index - 1, -1):
            list_of_targets.pop(removing_index)
    else:  # some of edge indexes is not valid
        print("Strike missed!")
    return list_of_targets


targets = [int(target) for target in input().split()]
command = input()
while command != "End":
    command = command.split()
    action, index, value = command[0], int(command[1]), int(command[2])
    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)
    command = input()
print(*targets, sep="|")