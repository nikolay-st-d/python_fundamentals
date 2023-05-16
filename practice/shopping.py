budget = int(input())

while True:
    com = input()

    if com != 'End':
        price = int(com)
        budget -= price
        if budget < 0:
            print('You went in overdraft!')
            break
    else:
        print('You bought everything needed.')
        break

