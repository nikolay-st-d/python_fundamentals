# 80/100 points, maybe it's the decrypt_regex
import re
decrypt_regex = r's|t|a|r'
match_regex = r'@([A-Za-z]*).*:([0-9]+).*!(A|D)!.*->([0-9]+)'
number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []
for _ in range(number_of_messages):
    raw_message = input()
    match = re.findall(decrypt_regex, raw_message, re.IGNORECASE)
    cipher = len(match)
    decrypted_message = ''
    for char in raw_message:
        new_char = chr(ord(char) - cipher)
        decrypted_message += new_char
    match = re.search(match_regex, decrypted_message)
    if match:
        planet, population, attack, soldiers = match.groups()
        if attack == 'A':
            attacked_planets.append(planet)
        elif attack == 'D':
            destroyed_planets.append(planet)

print(f"Attacked planets: {len(attacked_planets)}")
for attacked_planet in sorted(attacked_planets):
    print(f"-> {attacked_planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for destroyed_planet in sorted(destroyed_planets):
    print(f"-> {destroyed_planet}")

