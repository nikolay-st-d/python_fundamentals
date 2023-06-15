def merge(text, start_index, end_index):
    if start_index < 0:
        start_index = 0
    elif start_index > len(text):
        start_index = len(text) - 1
    if end_index > len(text):
        end_index = text.index(text[-1])
    merged_string = ''
    for index in range(start_index, end_index + 1):
        merged_string += text[index]
    text[start_index] = merged_string
    for element_index in range(end_index, start_index, -1):
        text.pop(element_index)
    return text


# def divide_element(text, element_index, partitions):
#     element = text[element_index]
#     strings_in_element = len(element)
#     new_str_length = strings_in_element // partitions
#     if element_index == 0:
#         pass
#     elif element_index == len(text) - 1:
#         pass
#     else:
#         pass

# function by Stoyan Stoyanov
def divide(input_text, current_index, partitions):
    new_sequence = []
    for index, word in enumerate(input_text):
        if current_index != index:
            new_sequence.append(word)
        else:
            if partitions > len(word):
                step = 1
            else:
                step = len(word) // partitions
            start = 0

            for parts in range(partitions):
                if parts == partitions - 1:
                    new_sequence.append(word[start:])
                    break
                else:
                    new_sequence.append(word[start: start + step])
                start += step
    return new_sequence


text_sequence = input().split()

while True:
    input_row = input()
    if input_row == '3:1':
        break
    else:
        command_list = input_row.split()
    command, start_i, end_i = command_list[0], int(command_list[1]), int(command_list[2])
    if command == 'merge':
        text_sequence = merge(text_sequence, start_i, end_i)
    elif command == 'divide':
        text_sequence = divide(text_sequence, start_i, end_i)

print(text_sequence)