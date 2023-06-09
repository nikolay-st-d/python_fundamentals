def data_type(type, input):
    result = None
    if type == "int":
        result = int(input) * 2
    elif type == "real":
        result = float(input) * 1.5
        result = f'{result:.2f}'
    elif type == "string":
        result = '$' + input + '$'
    return result


input_type = input()
input_data = input()

print(data_type(input_type, input_data))

