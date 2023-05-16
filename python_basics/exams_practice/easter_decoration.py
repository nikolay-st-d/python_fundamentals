clients = int(input())

all_totals = 0

for _ in range(clients):
    client_total = 0
    client_purchases = 0
    print_it = False

    while True:
        purchase = input()

        if purchase == 'Finish':
            print_it = True
            break

        if purchase == 'basket':
            client_purchases += 1
            client_total += 1.50
        elif purchase == 'wreath':
            client_purchases += 1
            client_total += 3.8
        elif purchase == 'chocolate bunny':
            client_purchases += 1
            client_total += 7

    if client_purchases % 2 == 0:
        client_total *= 0.8
    all_totals += client_total

    if print_it:
        print(f'You purchased {client_purchases} items for {client_total:.2f} leva.')

print(f'Average bill per client is: {all_totals / clients:.2f} leva.')
        