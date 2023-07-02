chars = input().split(', ')
ascii_chars = {char: ord(char) for char in chars}
print(ascii_chars)