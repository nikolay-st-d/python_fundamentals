# # task 1
#
# 1. Receive initial energy
# 2. Create a variable that's keeps track of the won battles
# 3. while we have energy or we receive end of game - read distance from console
# 4. Check if distance is less than energy
#   - increase won battles with 1
#   - decrease energy with distance
#   - check if battle is third
#   - increase energy with battles count

energy = int(input())
distance = input()

battles_won = 0

while distance != "End of battle":
    distance = int(distance)

    if energy >= distance and energy > 0:
        energy -= distance
        battles_won += 1

        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break

    distance = input()
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")

# task 2

# 1. Read people count from the console
# 2. Read cabins current state from the console
# 3. Iterate over every cabin and put as much people as possible in it(MAX 4)
    # - Find# free spaces in cabin(MAX size - current state of cabin = free spaces)
    # - Fill the cabin
    # - Decrease number of waiting people
    # - Check if there are no more people of cabins

MAX_SIZE = 4

people = int(input())
lift = [int(x) for x in input().split()]

for i in range(len(lift)):
    free_spaces = MAX_SIZE - lift[i]

    if people >= free_spaces:
        lift[i] += free_spaces
    else:
        lift[i] += people

    people -= free_spaces

    if people <= 0 and (i != len(lift) - 1 or lift[i] < MAX_SIZE):
        print("The lift has empty spots!")
        break
else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")

print(*lift)

# task 3

# 1. Read sequence of numbers from the console
# 2. Find the average num for this sequence
# 3. Find all numbers above the average num
# 4. Sort the new collection in descending order
# 5. Check if there are numbers in the new collection
# 6. Print the top 5 numbers from the collection

FIRST_COUNT = 5

numbers = [int(x) for x in input().split()]
avg_num = sum(numbers) / len(numbers)
filtered_nums = sorted([x for x in numbers if x > avg_num])  # filter(lambda x: x > avg_num, numbers)

if not filtered_nums:
    print("No")
else:
    # for i in range(FIRST_COUNT):
    #     if filtered_nums:
    #         print(filtered_nums.pop(), end=" ")
    print(*[filtered_nums.pop() for i in range(FIRST_COUNT) if filtered_nums])