number_of_prints = 5
sequence = [int(x) for x in input().split()]
average_value = sum(sequence) / len(sequence)
sorted_sequence = sorted([x for x in sequence if x > average_value])
for i in range(len(sorted_sequence), len(sorted_sequence) - number_of_prints - 1, -1):
    if i in range(len(sorted_sequence)):
        print(sorted_sequence[i], end=' ')
if not sorted_sequence:
    print('No!')
