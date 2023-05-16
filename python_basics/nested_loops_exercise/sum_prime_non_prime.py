primes = 0
nonprimes = 0

while True:
    data = input()

    if data == 'stop':
        print(f'Sum of all prime numbers is: {primes}')
        print(f'Sum of all non prime numbers is: {nonprimes}')
        break
    else:
        num = int(data)

        if num < 0:
            print('Number is negative.')
            continue

        is_nonprime = False
        for i in range(2, num):
            if num % i == 0:
                is_nonprime = True
                break

        if is_nonprime:
            nonprimes += num
        else:
            primes += num


