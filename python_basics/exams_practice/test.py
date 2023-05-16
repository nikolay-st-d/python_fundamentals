# for _ in range(5):
#     com = input('Input a result in format 3:0, 0:8, 0:0: ')
#
#     if com == 'end':
#         break
#
#     a = int(com[0])
#     b = int(com[2])
#
#     print(a)
#     print(b)
#
#     if a > b:
#         print('WIN')
#     if a < b:
#         print('LOST')
#     if a == b:
#         print('DRAWN')

email = input('Input your email address: ')
username, domain = email.split('@')
print(f'Username: {username}', end=' | ')
print(f'Domain: {domain}')
