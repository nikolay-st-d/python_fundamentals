key = int(input())
num_of_lines = int(input())

dec_string = ''

for i in range(num_of_lines):
    letter = input()

    new_letter = chr(ord(letter) + key)
    dec_string += new_letter

print(dec_string)
