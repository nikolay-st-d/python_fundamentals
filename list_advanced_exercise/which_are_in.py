def is_substring_in_list(substring, string_list):
    for string in string_list:
        if substring in string:
            return True
    return False


first_list = input().split(', ')
second_list = input().split(', ')
result_list = []
for element in first_list:
    if is_substring_in_list(element, second_list):
        result_list.append(element)
print(result_list)
