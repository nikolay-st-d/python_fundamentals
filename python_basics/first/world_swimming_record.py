from math import floor

world_record_time = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter
slowdown_sec = floor(distance / 15) * 12.5
new_total_time = total_time + slowdown_sec

if new_total_time < world_record_time:
    print(f'Yes, he succeeded! The new world record is {new_total_time:.2f} seconds.')
else:
    time_difference = new_total_time - world_record_time
    print(f'No, he failed! He was {time_difference:.2f} seconds slower.')
