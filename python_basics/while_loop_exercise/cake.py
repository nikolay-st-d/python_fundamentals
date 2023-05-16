cake_w = int(input())
cake_h = int(input())
cake_pieces = cake_w * cake_h

while True:
    com = input()

    if com == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break
    else:
        pieces_eaten = int(com)
        cake_pieces -= pieces_eaten

        if cake_pieces < 1:
            print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
            break
        