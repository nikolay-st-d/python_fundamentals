def threshold_calculator(data):
    regex = r'[0-9]'
    matches = re.findall(regex, data)
    multiplied_digits = 1
    for digit in matches:
        multiplied_digits *= int(digit)
    return multiplied_digits


def calculate_emoji_coolness(emoji_data):
    coolness = 0
    for letter in emoji_data:
        coolness += ord(letter)
    return coolness


import re

text = input()
cool_threshold = threshold_calculator(text)
pattern = r'(\:{2}|\*{2})([A-Z]{1}[a-z]{2,})\1'
valid_emojis = re.findall(pattern, text)
count_of_emojis = len(valid_emojis)
print(f"Cool threshold: {cool_threshold}")
print(f"{count_of_emojis} emojis found in the text. The cool ones are:")
for emoji in valid_emojis:
    emoji_quotes, emoji_text = emoji
    if calculate_emoji_coolness(emoji_text) > cool_threshold:
        print(emoji_quotes + emoji_text + emoji_quotes)
