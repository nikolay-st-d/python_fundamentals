import re

data = input()
regex = r'([|#]{1})([A-Za-z\s]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1([0-9]{1,5})\1'
matches = re.findall(regex, data)
total_calories = 0
for match in matches:
    total_calories += int(match[3])
print(f"You have food to last you for: {total_calories // 2000} days!")
for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")