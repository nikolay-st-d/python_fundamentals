city = input()
sales_volume = float(input())
comm = 0
if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        comm = 0.05
    elif 500 < sales_volume <= 1000:
        comm = 0.07
    elif 1000 < sales_volume <= 10000:
        comm = 0.08
    elif sales_volume > 10000:
        comm = 0.12
elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        comm = 0.045
    elif 500 < sales_volume <= 1000:
        comm = 0.075
    elif 1000 < sales_volume <= 10000:
        comm = 0.1
    elif sales_volume > 10000:
        comm = 0.13
elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        comm = 0.055
    elif 500 < sales_volume <= 1000:
        comm = 0.08
    elif 1000 < sales_volume <= 10000:
        comm = 0.12
    elif sales_volume > 10000:
        comm = 0.145
comm_value = sales_volume * comm
if (city == 'Sofia' or city == 'Varna' or city == 'Plovdiv') and sales_volume >= 0:
    print(f'{comm_value:.2f}')
else:
    print('error')
