text = input()
num = 0
for letter in text:
    if letter == 'a':
        num += 1
    elif letter == 'e':
        num += 2
    elif letter == 'i':
        num += 3
    elif letter == 'o':
        num += 4
    elif letter == 'u':
        num += 5
print(num)
