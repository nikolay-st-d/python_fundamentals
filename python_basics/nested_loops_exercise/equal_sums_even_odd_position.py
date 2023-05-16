# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     even = 0
#     odd = 0
#     num_to_str = str(i)
#     for j, position in enumerate(num_to_str):
#         if j % 2 == 0:
#             even += int(position)
#         else:
#             odd += int(position)
#     if even == odd:
#         print(i, end=' ')


a = int(input())
b = int(input())

for i in range(a, b + 1):
    even = 0
    odd = 0
    num_to_str = str(i)
    for j in range(len(num_to_str)):
        if j % 2 == 0:
            even += int(num_to_str[j])
        else:
            odd += int(num_to_str[j])
    if even == odd:
        print(i, end=' ')
