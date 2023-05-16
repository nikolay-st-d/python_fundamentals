bottles = int(input())
det_qty = bottles * 750

cycle_counter = 0
dishes = 0
pots = 0

while True:
    com = input()
    cycle_counter += 1

    if com == 'End':
        print(f'Detergent was enough!')
        print(f'{dishes} dishes and {pots} pots were washed.')
        print(f'Leftover detergent {det_qty} ml.')
        break
    else:
        vessels = int(com)

        if cycle_counter % 3 == 0:
            det_qty -= vessels * 15
            pots += vessels
        else:
            det_qty -= vessels * 5
            dishes += vessels
        if det_qty < 0:
            print(f'Not enough detergent, {abs(det_qty)} ml. more necessary!')
            break
