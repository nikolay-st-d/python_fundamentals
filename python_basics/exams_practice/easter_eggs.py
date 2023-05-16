eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
max_color = 0
color_max = 0

while eggs > 0:
    color = input()

    if color == 'red':
        red += 1
        eggs -= 1
        if red > max_color:
            max_color = red
            color_max = 'red'
    elif color == 'orange':
        orange += 1
        eggs -= 1
        if orange > max_color:
            max_color = orange
            color_max = 'orange'
    elif color == 'blue':
        blue += 1
        eggs -= 1
        if blue > max_color:
            max_color = blue
            color_max = 'blue'
    elif color == 'green':
        green += 1
        eggs -= 1
        if green > max_color:
            max_color = green
            color_max = 'green'

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_color} -> {color_max}")
