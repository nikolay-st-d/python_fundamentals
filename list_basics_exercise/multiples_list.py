factor = int(input())
count = int(input())

lst = []
last_num = 0

for _ in range(count):
    last_num += factor
    lst.append(last_num)

print(lst)