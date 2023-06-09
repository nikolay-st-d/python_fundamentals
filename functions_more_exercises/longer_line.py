def is_first_line_longer(line_1, line_2):
    """
    line_1 and line_2 are lists with coordinates of the two end pints of a line
    """
    if abs(min(line_1)) + abs(max(line_1)) > abs(min(line_2)) + abs(max(line_2)):
        return True
    return False


def print_closest_point(point_1, point_2):
    """
    point_1 and point_2 are lists with coordinates of the points
    the function prints the closest to the coordinate system zero point
    """
    point_1_print = ', '.join(map(str, point_1))
    point_2_print = ', '.join(map(str, point_2))
    if abs(min(point_1)) < abs(min(point_2)):
        print(f'({point_1_print})({point_2_print})')
    else:
        print(f'({point_2_print})({point_1_print})')


all_points = []
for _ in range(8):
    line_point = int(input())
    all_points.append(line_point)

first_line, second_line = all_points[:4], all_points[4:]

if is_first_line_longer(first_line, second_line):
    point_one, point_two = first_line[:2], first_line[2:]
    print_closest_point(point_one, point_two)
else:
    point_one, point_two = second_line[:2], second_line[2:]
    print_closest_point(point_one, point_two)






