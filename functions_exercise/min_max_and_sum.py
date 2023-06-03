data_list = input().split()
data_list_int = []
for element in data_list:
    data_list_int.append(int(element))

print(f'The minimum number is {min(data_list_int)}')
print(f'The maximum number is {max(data_list_int)}')
print(f'The sum number is: {sum(data_list_int)}')

