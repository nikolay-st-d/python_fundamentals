number_of_persons = int(input())
elevator_capacity = int(input())
counter = 0

while number_of_persons > 0:
    number_of_persons -= elevator_capacity
    counter += 1

print(counter)
