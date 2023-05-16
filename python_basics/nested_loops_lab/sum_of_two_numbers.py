start_num = int(input())
end_num = int(input())
mag_num = int(input())
seq_numb = 0
comb_counter = 0
is_mag_num_found = False

for i in range(start_num, end_num + 1):
    for j in range(start_num, end_num + 1):
        sum_numbers = i + j
        seq_numb += 1
        comb_counter += 1
        if sum_numbers == mag_num:
            is_mag_num_found = True
            print(f'Combination N:{seq_numb} ({i} + {j} = {mag_num})')

    if is_mag_num_found:
        break

if not is_mag_num_found:
    print(f'{comb_counter} combinations - neither equals {mag_num}')
