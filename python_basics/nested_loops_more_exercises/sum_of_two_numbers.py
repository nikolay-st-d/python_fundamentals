start = int(input())
end = int(input())
mag_num = int(input())

counter = 0
found = False

for a in range(start, end + 1):
    if found:
        break
    for b in range(start, end + 1):
        counter += 1
        if a + b == mag_num:
            print(f'Combination N:{counter} ({a} + {b} = {mag_num})')
            found = True
if not found:
    print(f'{counter} combinations - neither equals {mag_num}')
