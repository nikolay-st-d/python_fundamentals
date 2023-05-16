def is_even(num):
    if num % 2 == 0:
        return True
    return False


while True:
    a = int(input())

    if is_even(a):
        print(a)
