my_list = 'abcd efgh ijkl mnopqrst uvwx yz'.split(' ')
list_length = 22


def shorten_list(max_length, mylist):
    shortened_list = []
    last_element_str = []
    if len(mylist) < max_length:
        max_length = len(mylist)
    if len(mylist) >= max_length:
        shortened_list = [element for element in mylist if mylist.index(element) < max_length]
        last_element_str = ''.join([element for element in mylist if element not in shortened_list])
    shortened_list[-1] += last_element_str
    return shortened_list

def divide_element(index, partitions, list_of_str):
    element_index = int(index)
    partitions = int(partitions)
    element = list_of_str[element_index]
    str_in_element = len(element)
    new_str_length = str_in_element // partitions
    new_list_of_strings = [element[i:i + new_str_length] for i in range(0, len(element), new_str_length)]
    if len(new_list_of_strings[-1]) < new_str_length:
        new_list_of_strings[-2] += new_list_of_strings[-1]
        new_list_of_strings.pop(-1)
    left_list = list_of_str[:element_index]
    right_list = list_of_str[element_index + 1:]
    right_list.pop(-1)
    new_list_of_strings = shorten_list(partitions, new_list_of_strings)
    list_of_str = left_list + new_list_of_strings + right_list
    return list_of_str


print(divide_element(3, 2, my_list))