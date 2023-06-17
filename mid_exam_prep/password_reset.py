def take_odd(password_str):
    new_password = ''
    for i in range(len(password_str)):
        if i % 2 != 0:
            new_password += password_str[i]
    print(new_password)
    return new_password


def cut(password_str, index, length):
    str_to_remove = password_str[index:index+length]
    password_str = password_str.replace(str_to_remove, '', 1)
    print(password_str)
    return password_str


def substitute_substring(password_str, sub_str, subst):
    if sub_str in password_str:
        password_str = password_str.replace(sub_str, subst)
        print(password_str)
    else:
        print("Nothing to replace!")
    return password_str


password = input()
input_data = input()

while input_data != 'Done':
    if input_data == 'TakeOdd':
        password = take_odd(password)
    else:
        command_list = input_data.split()
        command = command_list[0]
        if command == 'Cut':
            target_index, str_length = int(command_list[1]), int(command_list[2])
            password = cut(password, target_index, str_length)
        elif command == 'Substitute':
            substring, substitute = command_list[1], command_list[2]
            password = substitute_substring(password, substring, substitute)


    input_data = input()

print(f"Your password is: {password}")