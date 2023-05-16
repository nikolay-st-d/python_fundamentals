while True:
    destination = input()
    if destination == 'End':
        break
    trip_budget = float(input())

    saved_money = 0

    while trip_budget >= saved_money:
        payment = float(input())
        saved_money += payment
        if trip_budget <= saved_money:
            print(f'Going to {destination}!')
            break
