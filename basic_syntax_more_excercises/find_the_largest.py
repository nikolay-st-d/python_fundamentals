number = int(input())

num_to_str = str(number)

sorted_list = sorted(list(num_to_str), reverse=True)

for i in sorted_list:
    print(i, end='')
