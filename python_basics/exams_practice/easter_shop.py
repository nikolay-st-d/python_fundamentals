eggs_stock = int(input())
eggs_sold = 0

while True:
    command = input()
    if command == 'Close':
        print('Store is closed!')
        print(f'{eggs_sold} eggs sold.')
        break
    eggs = int(input())
    if command == 'Buy':
        if eggs > eggs_stock:
            print('Not enough eggs in store!')
            print(f'You can buy only {eggs_stock}.')
            break
        else:
            eggs_stock -= eggs
            eggs_sold += eggs
    elif command == 'Fill':
        eggs_stock += eggs
