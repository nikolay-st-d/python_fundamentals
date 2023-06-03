# def string_multiplier(string, multiplier):
#     return string * multiplier


input_string = input()
multiplier = int(input())

multiplied = lambda string, mult: string * mult

# print(string_multiplier(input_string, current_multiplier))
print(multiplied(input_string, multiplier))