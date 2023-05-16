threshold = int(input())

grades_sum = 0
assignments_number = 0
last_assignment = ''
failed_grades = 0

while True:
    exam_name = input()

    if exam_name == 'Enough':
        print(f"Average score: {grades_sum / assignments_number:.2f}")
        print(f"Number of problems: {assignments_number}")
        print(f"Last problem: {last_assignment}")
        break

    grade = int(input())
    grades_sum += grade
    assignments_number += 1
    last_assignment = exam_name

    if grade <= 4:
        failed_grades += 1
    if failed_grades == threshold:
        print(f'You need a break, {failed_grades} poor grades.')
        break

