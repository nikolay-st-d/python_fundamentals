from sys import maxsize

min_num = maxsize

while True:
    string = input()

    if string == 'Stop':
        break

    num = int(string)

    if num < min_num:
        min_num = num

print(min_num)