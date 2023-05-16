money_needed = float(input())
money_balance = float(input())

days_spending = 0
total_days = 0

while True:
    action = input()
    sum_to = float(input())

    if action == 'spend':
        money_balance -= sum_to
        days_spending += 1
        total_days +=1
        if money_balance < 0:
            money_balance = 0
        if days_spending == 5:
            print("You can't save the money.")
            print(total_days)
            break
    elif action == 'save':
        money_balance += sum_to
        days_spending = 0
        total_days += 1
        if money_balance >= money_needed:
            print(f'You saved the money for {total_days} days.')
            break
