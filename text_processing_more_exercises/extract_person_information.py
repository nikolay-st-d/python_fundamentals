import re

number_of_lines = int(input())
for _ in range(number_of_lines):
    text = input()
    regex_name = r'@([A-Za-z]+)\|'
    regex_age = r'\#(\d+)\*'
    name = re.search(regex_name, text).group(1)
    age = re.search(regex_age, text).group(1)
    if name and age:
        print(f"{name} is {age} years old.")
