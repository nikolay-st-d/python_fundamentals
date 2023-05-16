name = input()

current_grade = 0
years = 0
total_grades = 0
failed = 0

while True:
    current_grade = float(input())

    if current_grade >= 4:
        total_grades += current_grade
        years += 1
    else:
        failed += 1

    if failed > 1:
        print(f'{name} has been excluded at {years + 1} grade')
        break

    elif years == 12:
        print(f'{name} graduated. Average grade: {total_grades / years:.2f}')
        break
