def sum_numbers(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2, number_3):
    result = sum_numbers(number_1, number_2) - number_3
    return result


def add_and_subtract():
    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())

    print(subtract(number_1, number_2, number_3))


add_and_subtract()
