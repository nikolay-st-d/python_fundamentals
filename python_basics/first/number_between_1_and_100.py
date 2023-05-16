num = int(input('Input a number between 1 and 100: '))
while num < 1 or num > 100:
    if (num < 1):
        print ('Invalid number!!! The number is LOWER than 1!')
    if (num > 100):
        print('Invalid number!!! The number is GREATER than 100!')
    num = int(input('Try another number to check if it is between 1 and 100: '))
print ('The number is:', num, 'and it is between 50 and 100: ')