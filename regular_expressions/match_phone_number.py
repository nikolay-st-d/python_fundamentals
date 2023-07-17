import re
data = input()
regex = '\+359 2 \d{3} \d{4}\\b|\+359-2-\d{3}-\d{4}\\b'
result = re.findall(regex, data)
print(', '.join(result))