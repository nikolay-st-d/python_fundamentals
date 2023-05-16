string = input()
lst = list(string.split(', '))
reversed_list = lst.copy()
reversed_list.reverse()
len_lst = len(lst)
# print(f'List: {lst}')
# print(f'Reversed List: {reversed_list}')
# print(f'List Len: {len_lst}')

if lst[len_lst - 1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for animal in reversed_list:
        wolf_index = reversed_list.index('wolf')
        print(f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!")
        break
