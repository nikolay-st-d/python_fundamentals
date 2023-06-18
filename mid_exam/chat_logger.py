data = input()
chat = []

while data != 'end':

    data_list = data.split()
    command = data_list[0]
    message = data_list[1]

    if command == 'Chat':
        chat.append(message)
    elif command == 'Delete':
        if message in chat:
            chat.remove(message)
    elif command == 'Edit':
        new_message = data_list[2]
        if message in chat:
            message_index = chat.index(message)
            chat[message_index] = new_message
    elif command == 'Pin':
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif command == 'Spam':
        list_of_messages = data_list[1:]
        for spam in list_of_messages:
            chat.append(spam)

    data = input()

print(*chat, sep='\n')