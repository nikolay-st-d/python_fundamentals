row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
num_row_1 = []
num_row_2 = []
num_row_3 = []
for element_1 in row_1:
    num_row_1.append(int(element_1))
for element_2 in row_2:
    num_row_2.append(int(element_2))
for element_3 in row_3:
    num_row_3.append(int(element_3))
first_won = False
second_won = False

# horizontals check
if num_row_1.count(1) == len(num_row_1):
    first_won = True
elif num_row_1.count(2) == len(num_row_1):
    second_won = True
if num_row_2.count(1) == len(num_row_2):
    first_won = True
elif num_row_2.count(2) == len(num_row_2):
    second_won = True
if num_row_3.count(1) == len(num_row_3):
    first_won = True
elif num_row_3.count(2) == len(num_row_3):
    second_won = True

# verticals check
if num_row_1[0] == num_row_2[0] == num_row_3[0] and num_row_1[0] == 1:
    first_won = True
elif num_row_1[0] == num_row_2[0] == num_row_3[0] and num_row_1[0] == 2:
    second_won = True
if num_row_1[1] == num_row_2[1] == num_row_3[1] and num_row_1[1] == 1:
    first_won = True
elif num_row_1[1] == num_row_2[1] == num_row_3[1] and num_row_1[1] == 2:
    second_won = True
if num_row_1[2] == num_row_2[2] == num_row_3[2] and num_row_1[2] == 1:
    first_won = True
elif num_row_1[2] == num_row_2[2] == num_row_3[2] and num_row_1[2] == 2:
    second_won = True

# diagonals check
if num_row_1[0] == num_row_2[1] == num_row_3[2] and num_row_1[0] == 1:
    first_won = True
elif num_row_1[0] == num_row_2[1] == num_row_3[2] and num_row_1[0] == 2:
    second_won = True
if num_row_1[2] == num_row_2[1] == num_row_3[0] and num_row_1[2] == 1:
    first_won = True
elif num_row_1[2] == num_row_2[1] == num_row_3[0] and num_row_1[2] == 2:
    second_won = True

if first_won:
    print('First player won')
elif second_won:
    print('Second player won')
else:
    print('Draw!')