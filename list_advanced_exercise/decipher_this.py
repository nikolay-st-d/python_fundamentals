def decipher(input_word):
    first_letter_code = ''
    rest_of_word = ''
    for sign in input_word:
        if not sign.isalpha():
            first_letter_code += sign
        else:
            rest_of_word += sign
    new_word = chr(int(first_letter_code)) + rest_of_word
    new_word_list = list(new_word)
    new_word_list[1], new_word_list[-1] = new_word_list[-1], new_word_list[1]
    return ''.join(new_word_list)


secret_message_words = input().split()
deciphered_sequence = [decipher(word) for word in secret_message_words]
print(' '.join(deciphered_sequence))
