string_list = input().split(', ')
number_of_beggars = int(input())
list_len = len(string_list)
integers_list = []
for string in string_list:
    integers_list.append(int(string))

final_list = []
start_index = 0

while start_index < number_of_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, list_len, number_of_beggars):
        current_beggar_sum += integers_list[current_index]
    final_list.append(current_beggar_sum)
    start_index += 1

print(final_list)
