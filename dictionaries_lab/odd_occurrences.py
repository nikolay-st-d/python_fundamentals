words_list = [word.lower() for word in input().split()]
words_dict = {}

for word in words_list:
    if word not in words_dict.keys():
        words_dict[word] = 1
    else:
        words_dict[word] += 1

for key in words_dict.keys():
    if words_dict[key] % 2 != 0:
        print(f'{key}', end=' ')
