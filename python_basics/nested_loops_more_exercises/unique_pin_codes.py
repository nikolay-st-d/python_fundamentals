# is_nonprime = False
#         for i in range(2, num):
#             if num % i == 0:
#                 is_nonprime = True
#                 break

limit_a = int(input())
limit_b = int(input())
limit_c = int(input())

for a in range(2, limit_a + 1):
    if a % 2 == 0:
        print_a = a
    else:
        continue
    for b in range(2, limit_b + 1):
        no_prime = True
        for i in range(2, b):
            if b % i == 0:
                no_prime = False
                break
        if no_prime:
            print_b = b
        else:
            continue
        for c in range(2, limit_c + 1):
            if c % 2 == 0:
                print_c = c
            else:
                continue

            print(a, b, c)
