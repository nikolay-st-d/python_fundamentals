string = input().upper()
temp_string = ''
final_string = ''
multiplier = ''
for index in range(len(string)):
    current_char = string[index]
    if not current_char.isdigit():
        temp_string += current_char
    else:
        for next_index in range(index, len(string)):
            if not string[next_index].isdigit():
                break
            multiplier += string[next_index]
        final_string += temp_string * int(multiplier)
        temp_string = ''
        multiplier = ''
unique_symbols = len(set(final_string))
print(f'Unique symbols used: {unique_symbols}')
print(final_string)

# Ivan Shopov resolution:
# text = input().upper()
# unique_symbols = ""
# current_symbol = ""
# repetitions = ""
# for index in range(len(text)):
#     if not text[index].isdigit():
#         current_symbol += text[index]
#     else:  # text[index] is digit -> working with repetitions
#         for next_symbols_index in range(index, len(text)):
#             if not text[next_symbols_index].isdigit():
#                 break
#             repetitions += text[next_symbols_index]
#         unique_symbols += current_symbol * int(repetitions)
#         current_symbol = ""
#         repetitions = ""
# print(f"Unique symbols used: {len(set(unique_symbols))}")
# print(unique_symbols)