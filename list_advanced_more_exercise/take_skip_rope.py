input_list = list(input())

numbers_list = [int(num) for num in input_list if num.isdigit()]
take_list = []
skip_list = []
chars_list = [ch for ch in input_list if not ch.isdigit()]

for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])

result = []

for i in range(len(take_list)):
    take = take_list[i]
    result += chars_list[:take]
    chars_list = chars_list[take:]
    skip = skip_list[i]
    chars_list = chars_list[skip:]

print(*result, sep='')
