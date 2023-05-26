cards_input = input()
card_list = cards_input.split(' ')
team_a = []
team_b = []
terminated = False

for card in card_list:
    if card[0] == 'A' and card not in team_a:
        team_a.append(card)
    elif card[0] == 'B' and card not in team_b:
        team_b.append(card)

    if len(team_a) > 4 or len(team_b) > 4:
        terminated = True
        break

print(f'Team A - {11 - len(team_a)}; Team B - {11 - len(team_b)}')
if terminated:
    print('Game was terminated')

