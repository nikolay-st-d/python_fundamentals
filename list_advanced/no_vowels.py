vowels = ['a', 'o', 'u', 'e', 'i']
string = input()
new_string = [letter for letter in string if letter.lower() not in vowels]
print(''.join(new_string))