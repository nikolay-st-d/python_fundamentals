# def tribonacci_sequence(n):
#     sequence = [1]
#     for i in range(1, n):
#         if len(sequence) < 3:
#             sequence.append(i)
#         else:
#             sequence.append(sum(sequence[-3:]))
#     return ' '.join([str(num) for num in sequence])


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = list(map(lambda x: x**2, lst))
print(new_list)

second_list = [num + 1 for num in new_list]
print(second_list)

string = 'Jason'
new_string = list(map(lambda x: x.upper(), string))
print('.'.join(new_string))