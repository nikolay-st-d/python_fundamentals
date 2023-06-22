numbers = [int(num) for num in input().split()]

while True:
    input_data = input()

    if input_data == 'Finish':
        print(*numbers)
        break
    input_data = input_data.split()

    command = input_data[0]

    if command == 'Add':
        num_to_append = int(input_data[1])
        numbers.append(num_to_append)
    elif command == 'Remove':
        numbers.remove(int(input_data[1]))
    elif command == 'Replace':
        value = int(input_data[1])
        replacement = int(input_data[2])
        if value in numbers:
            element_index = numbers.index(value)
            numbers[element_index] = replacement
    elif command == 'Collapse':
        border_value = int(input_data[1])
        numbers = [num for num in numbers if num >= border_value]