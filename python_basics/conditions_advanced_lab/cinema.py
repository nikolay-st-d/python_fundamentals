screening_type = input()
rows = int(input())
columns = int(input())
places = rows * columns
ticket_price = 0
if screening_type == 'Premiere':
    ticket_price = 12.00
elif screening_type == 'Normal':
    ticket_price = 7.50
elif screening_type == 'Discount':
    ticket_price = 5
print(f'{places * ticket_price:.2f} leva')
