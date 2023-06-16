first_desk_capacity_per_hour = int(input())
second_desk_capacity_per_hour = int(input())
third_desk_capacity_per_hour = int(input())
students = int(input())
common_desks_capacity = first_desk_capacity_per_hour + second_desk_capacity_per_hour + third_desk_capacity_per_hour
hours = 0

while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue

    students -= common_desks_capacity


print(f"Time needed: {hours}h.")
