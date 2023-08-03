start_char = ord(input())
end_char = ord(input())
text = input()

sum_of_codes = 0

for char in text:
    char_num = int(ord(char))
    if start_char < char_num < end_char:
        sum_of_codes += char_num
print(sum_of_codes)
