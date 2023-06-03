strings_sequence = input().split()
numbers_list = []
for number in strings_sequence:
    numbers_list.append(int(number))

list_middle = len(numbers_list) // 2
left = numbers_list[0:list_middle]
right = numbers_list[list_middle + 1:]
left_score = 0
right_score = 0

for left_element in left:
    left_score += left_element
    if left_element == 0:
        left_score *= 0.8
for right_element in reversed(right):
    right_score += right_element
    if right_element == 0:
        right_score *= 0.8

if left_score < right_score:
    print(f'The winner is left with total time: {left_score:.1f}')
else:
    print(f'The winner is right with total time: {right_score:.1f}')