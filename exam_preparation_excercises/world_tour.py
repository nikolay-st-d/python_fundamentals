def add_stop(input_string, command_data):
    index = int(command_data[1])
    insert_string = command_data[2]
    if index < len(input_string):
        left_part = input_string[:index]
        right_part = input_string[index:]
        input_string = left_part + insert_string + right_part
    return input_string


def remove_stop(input_string, command_data):
    start_index = int(command_data[1])
    end_index = int(command_data[2])
    if start_index < len(input_string) and end_index < len(input_string):
        left_part = input_string[:start_index]
        right_part = input_string[end_index + 1:]
        input_string = left_part + right_part
    return input_string


def switch(input_string, command_data):
    old_string = command_data[1]
    new_string = command_data[2]
    if old_string in input_string:
        final_string = input_string.replace(old_string, new_string)
        return final_string


string = input()
while True:
    data = input()
    if data == 'Travel':
        break
    command = data.split(':')
    action = command[0]
    if action == 'Add Stop':
        string = add_stop(string, command)
        print(string)
    elif action == 'Remove Stop':
        string = remove_stop(string, command)
        print(string)
    elif action == 'Switch':
        string = switch(string, command)
        print(string)
print(f'Ready for world tour! Planned stops: {string}')
