string = input()
letters = ''
digits = ''
others = ''
for s in string:
    if s.isalpha():
        letters += s
    elif s.isdigit():
        digits += s
    else:
        others += s
print(digits)
print(letters)
print(others)