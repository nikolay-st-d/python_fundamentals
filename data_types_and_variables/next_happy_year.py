number = int(input())
next_num = number

while True:
    found = True
    next_num += 1
    next_num_to_str = str(next_num)
    num_len = len(next_num_to_str)
    last_digit = 0
    new_num = ''
    for i in range(num_len):
        digit = int(next_num_to_str[i])
        if digit == last_digit:
            found = False
            break
        else:
            last_digit = digit
            new_num += str(digit)

    if found:
        print(new_num)
        break


