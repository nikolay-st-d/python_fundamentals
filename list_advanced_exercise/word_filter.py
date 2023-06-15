words_list = input().split()
filtered_list = list(word for word in words_list if len(word) % 2 == 0)
for element in filtered_list:
    print(element)