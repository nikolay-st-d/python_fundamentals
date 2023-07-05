string_list = input().split()
new_string = ''
for string in string_list:
    new_string += string * len(string)
print(new_string)
