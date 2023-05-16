paper_rolls = int(input())
fabric_rolls = int(input())
glue_lt = float(input())
discount = int(input())

price = paper_rolls * 5.8 + fabric_rolls * 7.2 + glue_lt * 1.2
price -= price * discount / 100

print(f'{price:.3f}')
