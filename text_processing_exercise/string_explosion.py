str_list = list(input())
for element in str_list:
    if element == '>':
        index = str_list.index(element)
        power = str_list[index + 1]
