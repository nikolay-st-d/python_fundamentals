all_students = {}
while True:
    data = input()
    if data == 'end':
        break
    course, student = data.split(' : ')
    if course not in all_students.keys():
        all_students[course] = [student]
    else:
        all_students[course].append(student)
for course, students_list in all_students.items():
    print(f"{course}: {len(students_list)}")
    for student_name in students_list:
        print(f"-- {student_name}")