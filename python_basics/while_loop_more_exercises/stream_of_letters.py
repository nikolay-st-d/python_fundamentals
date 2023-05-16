c_count = 0
o_count = 0
n_count = 0
letter = ''
word = ''
text = ''

while True:
    inp = input()

    if inp == 'End':
        print(text)
        break

    if inp.isalpha():
        letter = inp
    else:
        letter = ''

    if letter == 'c' and c_count == 0:
        c_count = 1
        letter = ''
    if letter == 'o' and o_count == 0:
        o_count = 1
        letter = ''
    if letter == 'n' and n_count == 0:
        n_count = 1
        letter = ''
    if c_count == 1 and o_count == 1 and n_count == 1:
        word += ' '
        c_count = 0
        o_count = 0
        n_count = 0
        text += word
        word = ''

    word += letter

