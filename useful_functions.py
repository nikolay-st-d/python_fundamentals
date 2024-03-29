def is_even(num):
    if num % 2 == 0:
        return True
    return False


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def replace_char_at_index(string, index=0, replacement=''):
    return f'{string[:index]}{replacement}{string[index+1:]}'


def insert_text_at_index(text, index=0, replacement=''):
    return f'{text[:index + 1]}{replacement}{text[index + 1:]}'


def email_splitter(email):
    username, domain = email.split('@')
    print(f'Username: {username}', end=' | ')
    print(f'Domain: {domain}')


def morse_to_latin_word(morse_word, morse_dict):
    decoded_word = ''
    morse_letters = morse_word.split(' ')
    for morse_letter in morse_letters:
        if morse_letter in morse_code_dict.keys():
            decoded_word += morse_dict[morse_letter]
        else:
            return f'<Error! Morse character not in morse codes dictionary!>'
    return decoded_word


morse_code_dict = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
                   "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
                   "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
                   "-.--": "Y", "--..": "Z"}