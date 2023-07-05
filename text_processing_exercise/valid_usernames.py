def check_alphanum(user_name):
    for letter in user_name:
        if not letter.isalnum() and letter != '-' and letter != '_':
            return False
    return True

usernames = input().split(', ')
for username in usernames:
    if 3 <= len(username) <= 16 and check_alphanum(username):
        print(username)