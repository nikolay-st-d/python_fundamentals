data = list(input())
for i in range(len(data) - 1, 0, -1):
    if data[i] == data[i - 1]:
        data.pop(i)
print(*data, sep='')