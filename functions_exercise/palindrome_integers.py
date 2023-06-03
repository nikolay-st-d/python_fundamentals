def is_palindrome(str):
    if str == str[::-1]:
        return True
    return False


data_list = input().split(', ')

for string in data_list:
    print(is_palindrome(string))


