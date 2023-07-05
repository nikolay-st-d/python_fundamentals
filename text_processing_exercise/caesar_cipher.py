data = input()
encrypted_data = ''
for char in data:
    encrypted_data += chr(ord(char) + 3)
print(encrypted_data)