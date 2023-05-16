tabs = int(input())
salary = float(input())
curr_salary = salary

for _ in range(tabs):
    tab = input()
    if tab == 'Facebook':
        curr_salary -= 150
    elif tab == 'Instagram':
        curr_salary -= 100
    elif tab == 'Reddit':
        curr_salary -= 50
    if curr_salary <= 0:
        print('You have lost your salary.')
        break

if curr_salary > 0:
    print(int(curr_salary))
