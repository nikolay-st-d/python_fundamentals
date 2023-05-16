number = int(input())
num = number

while True:
    found = True
    count = 0
    num += 1
    num_to_str = str(num)
    for digit in range(10):
        count = num_to_str.count(str(digit))
        if count > 1:
            found = False
            break
    if found:
        print(num_to_str)
        break


