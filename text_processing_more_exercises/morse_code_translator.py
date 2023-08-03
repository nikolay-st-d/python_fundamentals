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

decoded_words = []
morse_words = input().split(' | ')
for word in morse_words:
    decoded_words.append(morse_to_latin_word(word.strip(), morse_code_dict))
print(*decoded_words)
