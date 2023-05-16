season = input()  # “Winter”, “Spring”, “Summer”
group = input()  # “boys”, “girls”, “mixed”
students = int(input())
nights = int(input())

price = 0
sport = ''

if season == 'Winter':
    if group == 'girls':
        price = 9.6
        sport = 'Gymnastics'
    elif group == 'boys':
        price = 9.6
        sport = 'Judo'
    elif group == 'mixed':
        price = 10
        sport = 'Ski'
elif season == 'Spring':
    if group == 'girls':
        price = 7.2
        sport = 'Athletics'
    elif group == 'boys':
        price = 7.2
        sport = 'Tennis'
    elif group == 'mixed':
        price = 9.5
        sport = 'Cycling'
elif season == 'Summer':
    if group == 'girls':
        price = 15
        sport = 'Volleyball'
    elif group == 'boys':
        price = 15
        sport = 'Football'
    elif group == 'mixed':
        price = 20
        sport = 'Swimming'

total = price * students * nights

if students >= 50:
    total *= 0.5
elif 20 <= students < 50:
    total *= 0.85
elif 10 <= students < 20:
    total *= 0.95

print(f'{sport} {total:.2f} lv.')