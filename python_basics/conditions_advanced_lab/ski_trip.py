days = int(input())  # 0 - 365
room = input()  # "room for one person", "apartment" or "president apartment"
feedback = input()  # "positive" or "negative"
total_price = 0
days -= 1
if room == 'room for one person':
    total_price = days * 18
elif room == 'apartment':
    total_price = days * 25
    if days < 10:
        total_price *= 0.7
    elif 10 <= days <= 15:
        total_price *= 0.65
    elif days > 15 :
        total_price *= 0.5
elif room == 'president apartment':
    total_price = days * 35
    if days < 10:
        total_price *= 0.9
    elif 10 <= days <= 15:
        total_price *= 0.85
    elif days > 15 :
        total_price *= 0.8
if feedback == 'positive':
    total_price *= 1.25
elif feedback == 'negative':
    total_price *= 0.9

print(f'{total_price:.2f}')
