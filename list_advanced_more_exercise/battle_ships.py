number_of_rows = int(input())
rows_list = []
for i in range(number_of_rows):
    row = [int(x) for x in input().split()]
    rows_list.append(row)
strikes_list = [strike for strike in input().split()]
counter = 0
for strike in strikes_list:
    row = int(strike[0])
    column = int(strike[2])
    target_row = rows_list[row]
    if target_row[column] > 0:
        target_row[column] -= 1
        if target_row[column] == 0:
            counter += 1
print(counter)
# print(rows_list)

