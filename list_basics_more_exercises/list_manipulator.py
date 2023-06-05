def if_even(num_input: int) -> bool:
    if num_input % 2 == 0:
        return True
    return False


numbers_list = []
data_list = input().split()
for number in data_list:
    numbers_list.append(int(number))
final_list = []
while True:
    temp_list = []
    command = input()
    if command == 'end':
        break
    if len(command.split()) == 2:
        com_1, com_2 = command.split()

        if com_1 == 'exchange':
            border_index = int(com_2)
            if border_index > len(numbers_list) or border_index < 0:
                print('Invalid index')
                continue
            left_list = numbers_list[0:border_index + 1]
            right_list = numbers_list[border_index + 1:]
            temp_list.extend(right_list)
            temp_list.extend(left_list)
            final_list = temp_list
            print(temp_list)

        elif com_1 == 'max' or com_1 == 'min':
            even_list = []
            odd_list = []
            for num in numbers_list:
                if if_even(num):
                    even_list.append(num)
                else:
                    odd_list.append(num)

            # if com_1 == 'max' and com_2 == 'even':
            #     max_num = max(even_list)
            #     print(even_list.index(max_num))
            # elif com_1 == 'max' and com_2 == 'odd':
            #     max_num = max(odd_list)
            #     print(odd_list.index(max_num))
            # elif com_1 == 'min' and com_2 == 'even':
            #     min_num = min(even_list)
            #     print(even_list.index(min_num))
            # elif com_1 == 'min' and com_2 == 'odd':
            #     min_num = min(odd_list)
            #     print(odd_list.index(min_num))
            # else:
            #     print('No matches')

    elif len(command.split()) == 3:
        com_1, com_2, com_3 = command.split()
        # print(com_1, com_2, com_3)

print(numbers_list)