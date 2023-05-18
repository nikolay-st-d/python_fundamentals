people = int(input())
days = int(input())
coins = 0

for i in range(1, days + 1):

    if i % 10 == 0:
        people -= 2
    if i % 15 == 0:
        people += 5

    coins += 50
    coins -= people * 2

    if i % 3 == 0:
        coins -= people * 3
    if i % 5 == 0:
        coins += people * 20
        if i % 3 == 0:
            coins -= people * 2

print(f"{people} companions received {int(coins / people)} coins each.")
