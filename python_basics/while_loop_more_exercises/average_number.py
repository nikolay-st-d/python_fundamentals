n = int(input())
summ = 0
for i in range(n):
    num = int(input())
    summ += num
print(f'{summ / n:.2f}')