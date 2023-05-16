from sys import maxsize

max_num = -maxsize

while True:
    string = input()

    if string == 'Stop':
        break

    num = int(string)

    if num > max_num:
        max_num = num

print(max_num)
