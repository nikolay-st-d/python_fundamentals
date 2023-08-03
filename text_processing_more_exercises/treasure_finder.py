from math import ceil
import re


def decrypt(string, key):
    new_string = ''
    multiplier = ceil(len(string) / len(key))
    new_key = key * multiplier
    for i in range(len(string)):
        char_ascii_code = ord(string[i])
        decoded_char = chr(char_ascii_code - int(new_key[i]))
        new_string += decoded_char
    return new_string


decrypt_key = input().replace(' ', '')
message = input()
while message != 'find':
    decrypted_message = decrypt(message, decrypt_key)
    regex = r'&(\w+)&.*<(\w+)>'
    match = re.search(regex, decrypted_message)
    treasure = match.group(1)
    coordinates = match.group(2)
    print(f"Found {treasure} at {coordinates}")
    message = input()

