def iseven(num):
    if num % 2 == 0:
        return True
    return False


data_list = input().split()
data_list_int = []
for element in data_list:
    data_list_int.append(int(element))

filtered_list = list(filter(iseven, data_list_int))

print(filtered_list)

