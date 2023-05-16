from math import floor

h = float(input())
w = float(input())

rows = (w - 1) // 0.7
columns = h // 1.2
work_places = floor(rows * columns - 3)

print(work_places)
