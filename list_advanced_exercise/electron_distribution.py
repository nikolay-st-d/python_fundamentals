number_of_electrons = int(input())
shells_list = []
shell_number = 1
while number_of_electrons > 0:
    electrons_in_shell = 2 * shell_number ** 2
    if number_of_electrons >= electrons_in_shell:
        number_of_electrons -= electrons_in_shell
        shell_number += 1
        shells_list.append(electrons_in_shell)
    else:
        shells_list.append(number_of_electrons)
        break
print(shells_list)
