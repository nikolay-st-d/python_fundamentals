gift_list = input().split()
while True:
    command = input()
    if command == 'No Money':
        break
    gift = command.split()
    if gift[0] == 'OutOfStock':
        gift_element = gift[1]
        while gift_element in gift_list:
            element_index = gift_list.index(gift_element)
            gift_list[element_index] = 'None'
    elif gift[0] == 'Required':
        gift_element = gift[1]
        element_index = int(gift[2])
        if 0 <= element_index <= gift_list.index(gift_list[-1]):
            gift_list[element_index] = gift_element
    elif gift[0] == 'JustInCase':
        gift_element = gift[1]
        gift_list[-1] = gift_element
while 'None' in gift_list:
    gift_list.remove('None')
print(' '.join(gift_list))
