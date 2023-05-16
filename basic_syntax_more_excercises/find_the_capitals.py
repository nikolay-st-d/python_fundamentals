string = input()
i = 0
lst = []

for char in string:
    if char.isupper():
        lst.append(i)
    i += 1
print(lst)
