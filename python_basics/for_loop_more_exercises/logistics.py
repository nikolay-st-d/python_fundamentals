cargos = int(input())

van_tons = 0
truck_tons = 0
train_tons = 0

for i in range(cargos):
    weight = int(input())
    if weight <= 3:
        van_tons += weight
    elif 4 <= weight <= 11:
        truck_tons += weight
    else:
        train_tons += weight

total_tons = van_tons + truck_tons + train_tons
av_price = (van_tons * 200 + truck_tons * 175 + train_tons * 120) / total_tons

print(f'{av_price:.2f}')
print(f'{van_tons / total_tons * 100:.2f}%')
print(f'{truck_tons / total_tons * 100:.2f}%')
print(f'{train_tons / total_tons * 100:.2f}%')