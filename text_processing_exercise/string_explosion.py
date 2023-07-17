string = input()
result_string = ''
power = 0
for i in range(len(string)):
    if string[i] == '>':
        power += int(string[i + 1])
        result_string += '>'
    elif string[i] != '>' and power > 0:
        power -= 1
    else:
        result_string += string[i]
print(result_string)