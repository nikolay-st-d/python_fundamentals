control_min = int(input())  # minutes
control_sec = int(input())  # seconds
trace = float(input())
time_per_100m = int(input())  # seconds

record = control_min * 60 + control_sec

time = trace / 100 * time_per_100m
delay = trace / 120 * 2.5
time -= delay

if time <= record:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {time:.3f}.')
else:
    print(f'No, Marin failed! He was {time - record:.3f} second slower.')