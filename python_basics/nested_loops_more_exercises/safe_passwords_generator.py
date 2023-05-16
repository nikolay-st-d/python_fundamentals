fst = int(input())
snd = int(input())
max_pass = int(input())

end = False

for a in range(35, 56):
    if end:
        break
    for b in range(64, 97):
        if end:
            break
        for x in range(1, fst + 1):
            if end:
                break
            for y in range(1, snd + 1):
                print(f'{chr(a)}{chr(b)}{x}{y}{chr(b)}{chr(a)}', end='|')
                a += 1
                b += 1
                if a > 55:
                    a = 35
                if b > 96:
                    b = 64
                max_pass -= 1
                if max_pass == 0 or (x >= fst and y >= snd):
                    end = True
                    break



