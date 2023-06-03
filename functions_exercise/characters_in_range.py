def chars_in_range():
    char_1 = input()
    char_2 = input()

    num_1 = ord(char_1)
    num_2 = ord(char_2)

    for character_code in range(num_1 + 1, num_2):
        print(chr(character_code), end=' ')


chars_in_range()