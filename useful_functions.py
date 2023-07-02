def is_even(num):
    if num % 2 == 0:
        return True
    return False


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def replace_str_index(text, index=0, replacement=''):
    return f'{text[:index]}{replacement}{text[index+1:]}'


def email_splitter(email):
    username, domain = email.split('@')
    print(f'Username: {username}', end=' | ')
    print(f'Domain: {domain}')