city = input()
type_of_pack = input()
discount_vip = input()
days = int(input())

price = 0

if days > 7:
    days -= 1

if city == 'Bansko' or city == 'Borovets':
    if type_of_pack == 'withEquipment':
        if discount_vip == 'no':
            price = 100 * days
        elif discount_vip == 'yes':
            price = 100 * 0.90 * days
    elif type_of_pack == 'noEquipment':
        if discount_vip == 'no':
            price = 80 * days
        elif discount_vip == 'yes':
            price = 80 * 0.95 * days

elif city == 'Varna' or city == 'Burgas':
    if type_of_pack == 'withBreakfast':
        if discount_vip == 'no':
            price = 130 * days
        elif discount_vip == 'yes':
            price = 130 * 0.88 * days
    elif type_of_pack == 'noBreakfast':
        if discount_vip == 'no':
            price = 100 * days
        elif discount_vip == 'yes':
            price = 100 * 0.93 * days
if days < 1:
    print('Days must be positive number!')
if city != 'Bansko' and city != 'Borovets' and city != 'Varna' and city != 'Burgas' or type_of_pack != 'noEquipment' \
        and type_of_pack != 'withEquipment' and type_of_pack != 'withBreakfast' and type_of_pack != 'noBreakfast':
    print('Invalid input!')
elif price > 0:
    print(f'The price is {price:.2f}lv! Have a nice time!')
