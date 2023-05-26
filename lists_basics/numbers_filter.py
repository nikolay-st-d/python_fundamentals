n = int(input())

lst = []
filtered_lst = []

for _ in range(n):
    element = int(input())
    lst.append(element)

command = input()

for number in lst:
    if command == 'even':
        if number % 2 == 0:
            filtered_lst.append(number)
    elif command == 'odd':
        if number % 2 != 0:
            filtered_lst.append(number)
    elif command == 'positive':
        if number >= 0:
            filtered_lst.append(number)
    elif command == 'negative':
        if number < 0:
            filtered_lst.append(number)

print(filtered_lst)