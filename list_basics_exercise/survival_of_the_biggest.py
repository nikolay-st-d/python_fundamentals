list_of_numbers = input().split()
number_or_removals = int(input())
list_of_integers = []
final_list = []

for string_index in range(len(list_of_numbers)):
    list_of_integers.append(int(list_of_numbers[string_index]))

for _ in range(number_or_removals):
    smallest_int = min(list_of_integers)
    list_of_integers.remove(smallest_int)

for element in list_of_integers:
    final_list.append(str(element))

print(', '.join(final_list))

