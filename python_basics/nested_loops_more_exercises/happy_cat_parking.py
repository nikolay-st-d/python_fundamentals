days = int(input())
hours = int(input())


def even(n):
    if n % 2 == 0:
        return True
    return False


total = 0

for day in range(1, days + 1):

    day_price = 0

    for hour in range(1, hours + 1):
        price = 1
        if even(day) and not even(hour):
            price = 2.5
        if not even(day) and even(hour):
            price = 1.25
        day_price += price

    total += day_price
    print(f'Day: {day} - {day_price:.2f} leva')

print(f'Total: {total:.2f} leva')