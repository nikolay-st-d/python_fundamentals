from math import ceil

movie_name = input()
episode_minutes = int(input())
break_minutes = int(input())

lunch_time = break_minutes / 8
rest_time = break_minutes / 4
total_time_needed = episode_minutes + lunch_time + rest_time

if break_minutes >= total_time_needed:
    diff = break_minutes - total_time_needed
    print(f'You have enough time to watch {movie_name} and left with {ceil(diff)} minutes free time.')
else:
    diff = total_time_needed - break_minutes
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(diff)} more minutes.")
