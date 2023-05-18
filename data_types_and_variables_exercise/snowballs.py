number_of_balls = int(input())

h_weight = 0
h_time = 0
h_quality = 0
h_value = 0

for _ in range(number_of_balls):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality

    if value > h_value:
        h_weight = weight
        h_time = time
        h_quality = quality
        h_value = value

print(f"{h_weight} : {h_time} = {int(h_value)} ({h_quality})")
