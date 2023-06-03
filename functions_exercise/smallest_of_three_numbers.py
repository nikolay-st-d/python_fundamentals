def smallest_number_from_three(num_1, num_2, num_3):
    numbers_list = [num_1, num_2, num_3]
    smallest = min(numbers_list)
    return smallest


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(smallest_number_from_three(number_1, number_2, number_3))

