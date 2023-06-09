list_of_numbers = list(map(int, input().split(', ')))
index_list = []
for element in list_of_numbers:
    if element % 2 == 0:
        element_index = list_of_numbers.index(element)
        list_of_numbers[element_index] = 'no'
        index_list.append(element_index)
print(index_list)