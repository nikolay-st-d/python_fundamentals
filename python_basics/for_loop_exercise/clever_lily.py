age = int(input())
wm_price = float(input())
toy_price = int(input())

toys = 0
money = 0
sum_money = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money += 10
        sum_money += money - 1
    else:
        toys += 1

money_total = sum_money + toys * toy_price
diff = abs(wm_price - money_total)

if money_total >= wm_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
