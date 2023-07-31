def insert_text_at_index(text, index=0, replacement=''):
    return f'{text[:index + 1]}{replacement}{text[index + 1:]}'


txt = 'text text text'
indx = 3
replace_str = ' NEW TEXT'

print(insert_text_at_index(txt, indx, replace_str))