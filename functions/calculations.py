def operations_calculator(operation, num_1, num_2):
    result = 0
    if operation == 'multiply':
        result = num_1 * num_2
    elif operation == 'divide':
        if num_2 == 0:
            return 'ERROR: Division by zero!'
        else:
            result = int(num_1 / num_2)
    elif operation == 'add':
        result = num_1 + num_2
    elif operation == 'subtract':
        result = num_1 - num_2
    return result


operation_command = input()
number_1 = int(input())
number_2 = int(input())

print(operations_calculator(operation_command, number_1, number_2))
