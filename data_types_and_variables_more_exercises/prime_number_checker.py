number = int(input())
result = True

for i in range(2, number):
    if number % i == 0:
        result = False

print(result)
