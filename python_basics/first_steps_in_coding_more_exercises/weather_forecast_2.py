deg = float(input())

if 26 <= deg <= 35:
    print('Hot')
elif 20.1 <= deg <= 25.9:
    print('Warm')
elif 15 <= deg <= 20:
    print('Mild')
elif 12 <= deg <= 14.9:
    print('Cool')
elif 5 <= deg <= 11.9:
    print('Cold')
else:
    print('unknown')
