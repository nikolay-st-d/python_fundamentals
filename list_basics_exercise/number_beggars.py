# numbers_list = input().split(', ')
# beggars = int(input())
# new_list = [0] * beggars
# sum_i = 0
# for i in range(len(numbers_list)):
#     beggars_i = i % beggars
#     sum_i = int(numbers_list[i])
#     new_list[beggars_i] += sum_i
# print(new_list)

integers_string = input()
beggars = int(input())

for beggar in range(1, beggars + 1):
    print(beggar)
