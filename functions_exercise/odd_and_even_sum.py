number = input()


def odd_even_digits_in_number(num):
    even_list = []
    odd_list = []
    for current_digit in str(num):
        current_digit = int(current_digit)
        if current_digit % 2 == 0:
            even_list.append(int(current_digit))
        else:
            odd_list.append(int(current_digit))
    print(f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}")


odd_even_digits_in_number(number)
