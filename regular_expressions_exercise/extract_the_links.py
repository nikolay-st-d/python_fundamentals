import re
while True:
    text = input()
    if not text:
        break
    regex = r'w{3}\.[A-Za-z0-9\-]+\.[a-z\.]+\b'
    matches = re.findall(regex, text)
    for match in matches:
        print(match)