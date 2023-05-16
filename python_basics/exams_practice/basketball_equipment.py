year_tax = int(input())
boots = year_tax * 0.6
outfit = boots * 0.8
ball = outfit / 4
accessories = ball / 5

print(f'{year_tax + boots + outfit + ball + accessories:.2f}')