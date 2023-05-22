import random
print('*****************')
print('GUESS THE NUMBER!')
print('*****************')
computer_number = random.randint(1, 100)
counter = 0
while True:
    player_input = input('Please input a number between 1 and 100: ')
    if not player_input.isdigit():
        print('INVALID INPUT! You must input a number!')
        continue
    player_number = int(player_input)
    counter += 1
    if player_number > computer_number:
        print('You number is greater. Please input a lower number!')
    elif player_number < computer_number:
        print('You number is lower. Please input a greater number!')
    else:
        print(f'CONGRATS! You guessed the number on your {counter} try!')
        break
