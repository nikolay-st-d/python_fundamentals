tour_days = int(input())

# global
total_money_raised = 0

# day
win_day = 0
lose_day = 0
daily_money_raised = 0

# game
win_game = 0
lose_game = 0

for i in range(tour_days):
    while True:
        com = input()

        if com == 'Finish':
            if win_game > lose_game:
                win_day += 1
                daily_money_raised *= 1.1
            else:
                lose_day += 1

            total_money_raised += daily_money_raised

            win_game = 0
            lose_game = 0
            daily_money_raised = 0

            break
        else:
            result = input()

            if result == 'win':
                win_game += 1
                daily_money_raised += 20
            elif result == 'lose':
                lose_game += 1

# output
if win_day > lose_day:
    total_money_raised *= 1.2
    print(f'You won the tournament! Total raised money: {total_money_raised:.2f}')
elif win_day < lose_day:
    print(f'You lost the tournament! Total raised money: {total_money_raised:.2f}')

# Lora Ilieva solution
# tournament_days = int(input())
# win_counter = 0
# lose_counter = 0
# has_won = False
# total_money = 0
#
# for day in range(tournament_days):
#     money = 0
#     days_win = 0
#     days_lost = 0
#
#     while True:
#         sport = input()
#
#         if sport == "Finish":
#             break
#
#         command = input()
#
#         if command == "win":
#             win_counter += 1
#             days_win += 1
#             money += 20
#         elif command == "lose":
#             lose_counter += 1
#             days_lost += 1
#
#     if days_win > days_lost:
#         money *= 1.1
#
#     total_money += money
#
# if win_counter > lose_counter:
#     total_money *= 1.2
#     has_won = True
#
# if has_won:
#     print(f"You won the tournament! Total raised money: {total_money:.2f}")
# else:
#     print(f"You lost the tournament! Total raised money: {total_money:.2f}")