number_of_iterations = int(input())

tank_capacity = 255
water_in_tank = 0

for _ in range(number_of_iterations):
    water_to_poor = int(input())
    if tank_capacity < water_to_poor:
        print('Insufficient capacity!')
    else:
        water_in_tank += water_to_poor
        tank_capacity -= water_to_poor

print(water_in_tank)
