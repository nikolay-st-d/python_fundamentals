def extract_barcode(input_data):
    regex = r'([@]{1}[#]{1,})([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})([@]{1}[#]{1,})'
    match = re.search(regex, input_data)
    if match:
        matched_barcode = match.group(2)
        return matched_barcode


def filter_barcode(barcode_to_filter):
    barcode_data = ''
    group_data = ''
    for char in barcode_to_filter:
        if char.isalpha():
            barcode_data += char
        else:
            group_data += char
    if group_data == '':
        group_data = '00'
    return group_data


import re

numer_of_inputs = int(input())

for _ in range(numer_of_inputs):
    data = input()
    raw_barcode = extract_barcode(data)
    if raw_barcode is not None:
        product_group = filter_barcode(raw_barcode)
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
