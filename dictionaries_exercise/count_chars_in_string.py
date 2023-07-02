string = input()
chr_dict = {}
for char in string:
    if char != ' ':
        if char not in chr_dict.keys():
            chr_dict[char] = 1
        else:
            chr_dict[char] += 1
for key, value in chr_dict.items():
    print(f"{key} -> {value}")