number_of_strings = int(input())

for _ in range(number_of_strings):
    mystring = input()
    pure = True

    for char in mystring:
        if char == ',' or char == '.' or char == '_':
            pure = False
            break

    if pure:
        print(f"{mystring} is pure.")
    else:
        print(f"{mystring} is not pure!")
