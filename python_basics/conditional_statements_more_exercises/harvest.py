from math import floor, ceil

vineyard_area = int(input())
grape_per_sqm = float(input())
wine_for_sale = int(input())
workers = int(input())

grape_for_wine = vineyard_area * grape_per_sqm * 0.40
wine_production = grape_for_wine / 2.5


if wine_production < wine_for_sale:
    print(f'It will be a tough winter! More {floor(wine_for_sale - wine_production)} liters wine needed.')
elif wine_production >= wine_for_sale:
    print(f'Good harvest this year! Total wine: {ceil(wine_production)} liters.')
    print(f'{ceil(wine_production-wine_for_sale)} liters left -> {ceil((wine_production-wine_for_sale) / workers)} liters per person.')
