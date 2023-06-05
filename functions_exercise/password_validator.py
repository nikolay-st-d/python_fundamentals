def validate_password(password):
    valid_password = True
    if len(password) < 6 or len(password) > 10:
        valid_password = False
        print('Password must be between 6 and 10 characters')
    if not password.isalnum():
        valid_password = False
        print('Password must consist only of letters and digits')
    digit_counter = 0
    for letter in password:
        if letter.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        valid_password = False
        print('Password must have at least 2 digits')
    if valid_password:
        print('Password is valid')


password_to_check = input()
validate_password(password_to_check)