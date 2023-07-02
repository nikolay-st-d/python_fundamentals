students = dict()
course_to_look_for = ''

while True:
    data = input()
    if ':' not in data:
        course_to_look_for = data.replace('_', ' ')
        break
    name, student_id, course = data.split(':')
    students[student_id] = {name: course}

for st_id, student in students.items():
    for name, course in student.items():
        if course == course_to_look_for:
            print(f"{name} - {st_id}")