numbers_sequence = input().split()
new_list = []
for number in numbers_sequence:
    new_list.append(abs(float(number)))
print(new_list)