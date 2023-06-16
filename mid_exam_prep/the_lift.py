WAGON_CAPACITY = 4
people = int(input())
lift = [int(w) for w in input().split()]

for i in range(len(lift)):
    current_free_places = WAGON_CAPACITY - lift[i]
    if people >= current_free_places:
        lift[i] += current_free_places
    else:
        lift[i] += people

    people -= current_free_places

    if people < 0 and (lift[i] > 0 or lift[-1] > 0):
        print('The lift has empty spots!')
        break
if people > 0 and lift[-1] == WAGON_CAPACITY:
    print(f"There isn't enough space! {people} people in a queue!")

print(*lift)
