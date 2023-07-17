import re

data = input()
regex = '(^|(?<=\s))-?(0|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
matches = re.finditer(regex, data)
for result in matches:
    print(result.group(), end=' ')