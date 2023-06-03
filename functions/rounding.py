numbers_as_str = input().split()
list_of_numbers = []

for element in numbers_as_str:
    list_of_numbers.append(round(float(element)))

print(list_of_numbers)

