number_of_chars = int(input())

ascii_sum = 0

for _ in range(number_of_chars):
    char = input()
    ascii_num = ord(char)
    ascii_sum += ascii_num
print(f"The sum equals: {ascii_sum}")