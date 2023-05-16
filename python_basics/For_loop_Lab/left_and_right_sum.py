n = int(input())

left_sum = 0
right_sum = 0

for i in range(2):
    if i == 0:
        for num in range(n):
            left_sum += int(input())
    else:
        for num in range(n):
            right_sum += int(input())

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')
