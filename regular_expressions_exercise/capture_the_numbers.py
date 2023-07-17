import re
results = []
while True:
    string = input()
    if string == '':
        break
    regex = '\\d+'
    match = re.findall(regex, string)
    results += match
for element in results:
    print(element, end=' ')
