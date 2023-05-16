rest = float(input()) * 100
cycles = 0

while True:

    if rest >= 200:
        rest -= 200
        cycles += 1

    if rest >= 100:
        rest -= 100
        cycles += 1

    if rest >= 50:
        rest -= 50
        cycles += 1

    if rest >= 20:
        rest -= 20
        cycles += 1

    if rest >= 10:
        rest -= 10
        cycles += 1

    if rest >= 5:
        rest -= 5
        cycles += 1

    if rest >= 2:
        rest -= 2
        cycles += 1

    if rest >= 1:
        rest -= 1
        cycles += 1

    if rest < 1:
        print(cycles)
        break
