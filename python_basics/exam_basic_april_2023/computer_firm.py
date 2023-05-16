comps = int(input())

total_rating = 0
sales = 0

for _ in range(comps):

    data = int(input())

    rating = data % 10
    pot_sales = (data - rating) / 10
    total_rating += rating

    if rating == 2:
        sales += 0
    elif rating == 3:
        sales += pot_sales * 0.5
    elif rating == 4:
        sales += pot_sales * 0.7
    elif rating == 5:
        sales += pot_sales * 0.85
    elif rating == 6:
        sales += pot_sales


print(f'{sales: .2f}')
print(f'{total_rating / comps: .2f}')
