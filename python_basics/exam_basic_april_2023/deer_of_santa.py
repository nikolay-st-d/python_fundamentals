from math import floor
from math import ceil

days = int(input())
food_kg = int(input())
food_deer_one = float(input())
food_deer_two = float(input())
food_deer_three = float(input())

deer_one = days * food_deer_one
food_kg -= deer_one
deer_two = days * food_deer_two
food_kg -= deer_two
deer_three = days * food_deer_three
food_kg -= deer_three

if food_kg >= 0:
    print(f'{floor(food_kg)} kilos of food left.')
else:
    print(f'{ceil(abs(food_kg))} more kilos of food are needed.')
