n = int(input())
words_dict = dict()

for _ in range(n):
    word = input()
    synonym = input()
    if word not in words_dict.keys():
        words_dict[word] = [synonym]
    else:
        words_dict[word].append(synonym)
for key, synonyms in words_dict.items():
    print(f"{key} - {', '.join(synonyms)}")