from math import floor


def closest_point(x1, y1, x2, y2):
    point_1 = [x1, y1]
    point_2 = [x2, y2]
    if abs(min(point_1)) < abs(min(point_2)):
        point_1_print = f'({floor(point_1[0])}, {floor(point_1[1])})'
        print(point_1_print)
    else:
        point_2_print = f'({floor(point_2[0])}, {floor(point_2[1])})'
        print(point_2_print)

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

closest_point(x_1, y_1, x_2, y_2)

