hours = int(input())
minutes = int(input())
minutes_plus_15 = minutes + 15
if minutes_plus_15 >= 60:
    minutes = minutes_plus_15 - 60
    hours = hours + 1
if minutes_plus_15 < 60:
    minutes = minutes_plus_15
if hours == 24:
    hours = 0
if minutes <= 9:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')