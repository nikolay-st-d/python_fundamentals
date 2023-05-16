from math import floor, ceil

days = int(input())
food_stored = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

food_needed = days * (dog_food_per_day + cat_food_per_day + turtle_food_per_day / 1000)

diff = abs(food_needed - food_stored)

if food_needed < food_stored:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')