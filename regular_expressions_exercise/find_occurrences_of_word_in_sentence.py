import re

sentence = input()
searched_string = input()
regex = fr'(?i)\b({searched_string})+\b'
matches = re.findall(regex, sentence)
print(len(matches))