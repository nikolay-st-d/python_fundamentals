energy = 100
coins = 100
events_list = input().split('|')
closed = False
for current_event in events_list:
    event_name, event_value = current_event.split('-')
    event_value = int(event_value)
    if event_name == 'rest':
        current_energy = energy
        energy += event_value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event_name == 'order':
        if energy >= event_value:
            energy -= 30
            coins += event_value
            print(f'You earned {event_value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= event_value:
            coins -= event_value
            print(f'You bought {event_name}.')
        else:
            print(f'Closed! Cannot afford {event_name}.')
            closed = True
            break
if not closed:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')

