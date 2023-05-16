petar_budget = float(input())
vcard_pieces = int(input())
processor_pieces = int(input())
ram_pieces = int(input())

processor_price = vcard_pieces * 250 * 0.35
ram_price = vcard_pieces * 250 * 0.1

total = (vcard_pieces * 250) + (processor_pieces * processor_price) + (ram_pieces * ram_price)

if vcard_pieces > processor_pieces:
    total *= 0.85

budget_difference = petar_budget - total

if budget_difference >= 0:
    print(f'You have {budget_difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(budget_difference):.2f} leva more!')

