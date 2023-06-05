def perfect_number(number):
    divisors_list = []
    for digit in range(1, number):
        if number % digit == 0:
            divisors_list.append(digit)
    print(divisors_list)
    if sum(divisors_list) == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


number_to_check = int(input())

perfect_number(number_to_check)