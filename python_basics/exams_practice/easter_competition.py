number_breads = int(input())

top_chef = ''
top_chef_points = 0

for i in range(number_breads):
    chef = input()
    chef_points = 0
    top = False

    while True:
        data = input()

        if data != 'Stop':
            points = int(data)
            chef_points += points
            if chef_points > top_chef_points:
                top = True
                top_chef = chef
                top_chef_points = chef_points
        else:
            print(f'{chef} has {chef_points} points.')
            if top:
                print(f'{chef} is the new number 1!')
            break

print(f'{top_chef} won competition with {top_chef_points} points!')
