num_of_lines = int(input())

left = 0
left_iteration = 0
right = 0
right_iteration = 0

balanced = False

for i in range(num_of_lines):
    char = input()

    if char == '(':
        left += 1
        left_iteration = i
    elif char == ')':
        right += 1
        right_iteration = i

    if left == 1 and right == 1 and left_iteration < right_iteration:
        balanced = True
        left = 0
        left_iteration = 0
        right = 0
        right_iteration = 0

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

