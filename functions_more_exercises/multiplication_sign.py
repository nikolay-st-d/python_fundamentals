def multiplication_sign(num_1, num_2, num_3):
    list_of_integers = [num_1, num_2, num_3]
    list_of_signs = []
    for digit in list_of_integers:
        if digit == 0:
            list_of_signs.append('zero')
        elif digit > 0:
            list_of_signs.append('positive')
        elif digit < 0:
            list_of_signs.append('negative')
    if list_of_signs.count('zero') > 0:
        return 'zero'
    elif list_of_signs.count('negative') == 1 or list_of_signs.count('negative') == 3:
        return 'negative'
    elif list_of_signs.count('positive') == 3 or list_of_signs.count('negative') == 2:
        return 'positive'


a = int(input())
b = int(input())
c = int(input())

print(multiplication_sign(a, b, c))