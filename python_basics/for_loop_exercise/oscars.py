actor = input()
start_points = float(input())
n = int(input())

total_judges_points = 0
all_points = start_points

for i in range(n):
    judge = input()
    judge_points = float(input())
    total_judges_points = len(judge) * judge_points / 2
    all_points += total_judges_points
    if all_points > 1250.5:
        print(f'Congratulations, {actor} got a nominee for leading role with {all_points:.1f}!')
        break
if all_points <= 1250.5:
    print(f'Sorry, {actor} you need {1250.5 - all_points:.1f} more!')
