list_of_employees = list(map(int, input().split()))
improvement_factor = int(input())
number_of_employees = len(list_of_employees)
improved_happiness_list = [element * improvement_factor for element in list_of_employees]
average_happiness = sum(improved_happiness_list) / number_of_employees
happy_employees_list = [employee for employee in improved_happiness_list if employee >= average_happiness]
number_of_happy_employees = len(happy_employees_list)
if len(happy_employees_list) >= len(list_of_employees) / 2:
    print(f"Score: {number_of_happy_employees}/{number_of_employees}. Employees are happy!")
else:
    print(f"Score: {number_of_happy_employees}/{number_of_employees}. Employees are not happy!")