def validate_password(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        return 'Password must be between 6 and 10 characters'
