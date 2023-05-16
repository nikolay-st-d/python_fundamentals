# from string import ascii_lowercase as alc
# alphabet = list(alc)
# print(alphabet)


start_letter = input()
end_letter = input()
skip_letter = input()

combinations = 0

for a in range(ord(start_letter), ord(end_letter) + 1):
    for b in range(ord(start_letter), ord(end_letter) + 1):
        for c in range(ord(start_letter), ord(end_letter) + 1):
            to_print = chr(a) + chr(b) + chr(c)
            if skip_letter not in to_print:
                combinations += 1
                print(to_print, end=' ')
print(combinations)
