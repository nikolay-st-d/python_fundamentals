row_pairs = int(input())
students = {}
for _ in range(row_pairs):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)
for name, grade in students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        print(f"{name} -> {average_grade:.2f}")