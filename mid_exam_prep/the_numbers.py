number_of_prints = 5
sequence = [int(x) for x in input().split()]
average_value = sum(sequence) / len(sequence)
sorted_sequence = sorted([x for x in sequence if x > average_value], reverse=True)
final_list = sorted_sequence[:number_of_prints]
if not final_list:
    print('No')
else:
    print(*final_list)