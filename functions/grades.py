def grade_level_from_number(grade_number):
    if 2 <= grade_number <= 2.99:
        level = 'Fail'
    elif 3 <= grade_number <= 3.49:
        level = 'Poor'
    elif 3.50 <= grade_number <= 4.49:
        level = 'Good'
    elif 4.50 <= grade_number <= 5.49:
        level = 'Very Good'
    elif 5.50 <= grade_number <= 6:
        level = 'Excellent'
    return level


grade_input = float(input())
print(grade_level_from_number(grade_input))
