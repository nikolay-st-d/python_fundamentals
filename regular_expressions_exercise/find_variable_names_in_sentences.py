import re

text = input()
regex = '\\b_([A-Za-z0-9]+)\\b'
match = re.findall(regex, text)
print(','.join(match))