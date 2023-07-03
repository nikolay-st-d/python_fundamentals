phonebook = {}
n = 0
while True:
    data = input()

    if '-' not in data:
        n = int(data)
        break

    name, number = data.split('-')
    phonebook[name] = number

for _ in range(n):
    search = input()
    if search in phonebook:
        print(f'{search} -> {phonebook[search]}')
    else:
        print(f'Contact {search} does not exist.')