number_of_courses = int(input())
list_of_courses = []

for course in range(number_of_courses):
    course_name = input()

    list_of_courses.append(course_name)

print(list_of_courses)