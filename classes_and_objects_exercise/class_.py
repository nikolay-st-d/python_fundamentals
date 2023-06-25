class Class:
    __students_count = 22
    students = []
    grades = []

    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, grade: float):
        if len(Class.students) < Class.__students_count:
            Class.students.append(name)
            Class.grades.append(grade)

    def get_average_grade(self):
        return sum(Class.grades) / len(Class.grades)

    def __repr__(self):
        average_grade = Class.get_average_grade(self)
        return f"The students in {self.name}: {', '.join(Class.students)}. Average grade: {average_grade:.2f}"

# Test code
a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)