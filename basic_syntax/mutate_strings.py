str_1 = input()
str_2 = input()


def replace_str_index(text, index=0, replacement=''):
    return f'{text[:index]}{replacement}{text[index+1:]}'


previous_word = str_1

for i in range(len(str_1)):

    replacement_letter = str_2[i]
    # new_word = previous_word.replace(previous_word[i], replacement_letter)
    new_word = replace_str_index(previous_word, i, replacement_letter)

    if new_word != previous_word and new_word != str_1:
        previous_word = new_word
        print(new_word)


