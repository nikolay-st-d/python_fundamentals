string1, string2 = input().split()
first_string = string1
second_string = string2
if len(string1) > len(string2):
    first_string = string2
    second_string = string1
rest = second_string[len(first_string):]
result = 0
for i in range(len(first_string)):
    a = ord(first_string[i])
    b = ord(second_string[i])
    result += a * b
for letter in rest:
    result += ord(letter)
print(result)