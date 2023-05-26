string = input()
lst = string.split(' ')
new_list = []

for num in lst:
    digit = int(num)
    inverted = digit * -1
    new_list.append(inverted)

print(new_list)