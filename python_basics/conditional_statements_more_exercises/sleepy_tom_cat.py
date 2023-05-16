from math import floor

weekend_days = int(input())
work_days = 365 - weekend_days

play_time = work_days * 63 + weekend_days * 127
diff = abs(30000 - play_time)

play_hours = floor(diff / 60)
play_minutes = diff % 60

if play_time > 30000:
    print('Tom will run away')
    print(f'{play_hours} hours and {play_minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{play_hours} hours and {play_minutes} minutes less for play')
