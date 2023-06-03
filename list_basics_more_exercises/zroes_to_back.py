list_of_numbers = input().split(', ')
list_of_integers = []
list_of_zeroes = []
filtered_list = []
for element in list_of_numbers:
    list_of_integers.append(int(element))

for element in list_of_integers:
    if element == 0:
        list_of_zeroes.append(element)
    else:
        filtered_list.append(element)
print(filtered_list + list_of_zeroes)

