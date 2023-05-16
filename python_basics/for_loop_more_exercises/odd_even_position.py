from sys import maxsize

n = int(input())

sum_even = 0
max_even = -maxsize
min_even = maxsize

sum_odd = 0
max_odd = -maxsize
min_odd = maxsize

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        sum_even += num
        if num > max_even:
            max_even = num
        if num < min_even:
            min_even = num
    else:
        sum_odd += num
        if num > max_odd:
            max_odd = num
        if num < min_odd:
            min_odd = num

print(f"OddSum={sum_odd:.2f},")
if min_odd != maxsize:
    print(f"OddMin={min_odd:.2f},")
else:
    print('OddMin=No,')
if max_odd != -maxsize:
    print(f"OddMax={max_odd:.2f},")
else:
    print('OddMax=No,')

print(f"EvenSum={sum_even:.2f},")
if min_even != maxsize:
    print(f"EvenMin={min_even:.2f},")
else:
    print('EvenMin=No,')
if max_even != - maxsize:
    print(f"EvenMax={max_even:.2f}")
else:
    print('EvenMax=No')
