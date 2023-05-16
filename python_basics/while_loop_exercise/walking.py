goal = 10000

total_steps = 0

while True:
    command = input()

    if command == 'Going home':
        steps_home = int(input())
        total_steps += steps_home
        if total_steps <= goal:
            print(f'{goal - total_steps} more steps to reach goal.')
            break
        else:
            print(f'Goal reached! Good job!')
            print(f'{total_steps - goal} steps over the goal!')
            break
    else:
        walk_steps = int(command)
        total_steps += walk_steps
        if total_steps >= goal:
            print(f'Goal reached! Good job!')
            print(f'{total_steps - goal} steps over the goal!')
            break
