sum_expected = int(input())
money = 0
cycle_count = 0
cs = 0
cc = 0
cs_cust = 0
cc_cust = 0

while True:
    com = input()
    cycle_count += 1

    if com == 'End':
        print('Failed to collect required money for charity.')
        break
    else:
        price = int(com)

        if cycle_count % 2 != 0:  # Cash Payment
            if price > 100:
                print('Error in transaction!')
            else:
                money += price
                cs += price
                cs_cust += 1
                print('Product sold!')
        else:  # Card Payment
            if price < 10:
                print('Error in transaction!')
            else:
                money += price
                cc += price
                cc_cust += 1
                print('Product sold!')

    if money >= sum_expected:
        print(f'Average CS: {cs / cs_cust:.2f}')
        print(f'Average CC: {cc / cc_cust:.2f}')
        break
