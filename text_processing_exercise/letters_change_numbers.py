import string
alphabet = list(string.ascii_lowercase)

def process_first_letter(string):
    first_letter = string[0]
    number = int(string[1:-1])
    letter_position = alphabet.index(first_letter.lower()) + 1
    if first_letter.isupper():
        result_number = number / letter_position
    else:
        result_number = number * letter_position
    return result_number

def process_last_letter(string):
    last_letter = string[-1]
    # number = int(string[1:-1])
    number = process_first_letter(string)
    letter_position = alphabet.index(last_letter.lower()) + 1
    if last_letter.isupper():
        result_number = number - letter_position
    else:
        result_number = number + letter_position
    return result_number

data = [string.strip() for string in input().split()]

total_sum = 0

for element in data:
    temp_number = process_first_letter(element)
    current_number = process_last_letter(element)
    total_sum += current_number

print(f'{total_sum:.2f}')