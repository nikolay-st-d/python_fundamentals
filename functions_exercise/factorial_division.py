def factorial(number):
    factorial_number = 1
    for i in range(1, number + 1):
        factorial_number *= i
    return factorial_number


def factorial_division(num_1, num_2):
    result = factorial(num_1) / factorial(num_2)
    return result


number_one = int(input())
number_two = int(input())

print(f"{factorial_division(number_one, number_two):.2f}")
