best_player = ''
goals = 0
player_goals = 0
hat_trick = False

while True:
    name = input()
    if name == 'END':
        break
    goals = int(input())

    if goals > player_goals:
        player_goals = goals
        best_player = name

    if player_goals >= 3:
        hat_trick = True

    if goals >= 10:
        break

print(f'{best_player} is the best player!')
if hat_trick:
    print(f'He has scored {player_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {player_goals} goals.')
