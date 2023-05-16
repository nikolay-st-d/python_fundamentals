students = int(input())

students_5 = 0
students_4 = 0
students_3 = 0
students_2 = 0
total_grades = 0

for i in range(students):
    grade = float(input())
    total_grades += grade
    if grade >= 5:
        students_5 += 1
    elif 4 <= grade <= 4.99:
        students_4 += 1
    elif 3 <= grade <= 3.99:
        students_3 += 1
    else:
        students_2 += 1

print(f"Top students: {students_5 / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {students_4 / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {students_3 / students * 100:.2f}%")
print(f"Fail: {students_2 / students * 100:.2f}%")
print(f"Average: {total_grades / students:.2f}")
