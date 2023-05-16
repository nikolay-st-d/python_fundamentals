num = int(input())
is_finished = False
current_num = 0

for i in range(1, num + 1):
    for j in range(1, i + 1):
        current_num += 1
        if current_num > num:
            is_finished = True
            break
        print(current_num, end=' ')
    if is_finished:
        break
    print()
