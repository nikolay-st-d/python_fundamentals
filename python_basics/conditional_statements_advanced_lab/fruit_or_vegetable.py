name = input()
if name == 'banana' or name == 'apple' or name == 'kiwi' or name == 'cherry' or name == 'lemon' or name == 'grapes':
    f_type = 'fruit'
elif name == 'tomato' or name == 'cucumber' or name == 'pepper' or name == 'carrot':
    f_type = 'vegetable'
else:
    f_type = 'unknown'
print(f_type)
