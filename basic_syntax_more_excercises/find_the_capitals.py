string = input()
i = 0
my_list = []
for char in string:
    if char.isupper():
        my_list.append(i)
    i += 1
print(my_list)
