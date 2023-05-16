budget = float(input())
category = input()
people = int(input())

transport = 0
ticket_price = 0

if category == 'VIP':
    ticket_price = 499.99
elif category == 'Normal':
    ticket_price = 249.99

if people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.6
elif 10 <= people <= 24:
    transport = budget * 0.5
elif 25 <= people <= 49:
    transport = budget * 0.4
else:
    transport = budget * 0.25

tickets_total = people * ticket_price
total = tickets_total + transport

if budget >= total:
    print(f'Yes! You have {budget - total:.2f} leva left.')
else:
    print(f'Not enough money! You need {total - budget:.2f} leva.')