one = int(input())
two = int(input())
five = int(input())
amount = int(input())

for i in range(one + 1):
    for j in range(two + 1):
        for h in range(five + 1):
            if i + j * 2 + h * 5 == amount:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {h} * 5 lv. = {amount} lv.')
