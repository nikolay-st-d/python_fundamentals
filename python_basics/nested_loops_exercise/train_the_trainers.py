jury_members = int(input())

total_sum_assessments = 0
total_assessments_count = 0

while True:
    presentation = input()

    pres_sum_assessments = 0
    pres_assessments_count = 0

    if presentation == 'Finish':
        print(f"Student's final assessment is {total_sum_assessments / total_assessments_count:.2f}.")
        break

    for i in range(jury_members):
        assessment = float(input())
        pres_sum_assessments += assessment
        pres_assessments_count += 1
        total_sum_assessments += assessment
        total_assessments_count += 1

    print(f'{presentation} - {pres_sum_assessments / pres_assessments_count:.2f}.')
