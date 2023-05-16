from math import floor
from math import ceil

racket_price = float(input())
rackets = int(input())
boots = int(input())

price = rackets * racket_price
price += boots * racket_price / 6
price *= 1.2


print(f'Price to be paid by Djokovic {floor(price / 8)}')
print(f'Price to be paid by sponsors {ceil(price * 7 / 8)}')