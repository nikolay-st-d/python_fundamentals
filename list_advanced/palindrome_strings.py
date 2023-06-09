strings_list = input().split()
palindrome = input()
palindromes_list = []
found_counter = 0
for string in strings_list:
    if string == string[::-1]:
        palindromes_list.append(string)
    if string == palindrome:
        found_counter += 1
print(palindromes_list)
print(f'Found palindrome {found_counter} times')