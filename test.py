def bit_on_position(num, position):
    mask = 1 << position
    bit = num & mask
    return bit >> position

print(bit_on_position(1, 2))