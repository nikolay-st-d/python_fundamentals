import random
from colorama import Fore, Back, Style

rock = 'Rock'
scissors = 'Scissors'
paper = 'Paper'

print('Rock, Scissors and Paper game')
print(Fore.BLUE + '*****************************')
print('Choose R for rock, S for scissors or P for paper')
print('Make your bet and press ENTER.')
print('If you want to terminate the game, please input "END"')

while True:
    print(Style.RESET_ALL)
    my_choice = input('Your bet: ')

    if my_choice.lower() == 'end':
        raise SystemExit('End of game!')

    if my_choice.lower() == 'r':
        user_bet = rock
    elif my_choice.lower() == 's':
        user_bet = scissors
    elif my_choice.lower() == 'p':
        user_bet = paper
    else:
        print('Invalid output! Please try again!')
        continue

    bets_list = ['Rock', 'Scissors', 'Paper']
    computer_bet = random.choice(bets_list)

    if user_bet == computer_bet:
        print(Fore.YELLOW + f'Draw')
    elif user_bet == rock and computer_bet == 'Scissors' or \
        user_bet == scissors and computer_bet == 'Paper' or \
            user_bet == paper and computer_bet == 'Rock':
        print(Fore.GREEN + f'You chose {user_bet},\nthe computer chose {computer_bet}.\nYOU WON!')
    else:
        print(Fore.RED + f'You chose {user_bet},\nthe computer chose {computer_bet}. \nYOU LOOSE!')

