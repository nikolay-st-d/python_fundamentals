number_strings = input().split()
text_string = input()
numbers = []
letters = []
for num in number_strings:
    sum_of_digits = 0
    for digit in num:
        sum_of_digits += int(digit)
    numbers.append(sum_of_digits)

for char in text_string:
    letters.append(char)

for number in numbers:
    if number >= len(letters):
        number -= len(letters)
    print(letters[number], end='')
    letters.remove(letters[number])

