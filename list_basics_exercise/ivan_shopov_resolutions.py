# 1

list_of_numbers = input().split()
opposite_numbers = []
for element in list_of_numbers:
    current_number = -int(element)
    opposite_numbers.append(current_number)
print(opposite_numbers)

# 2
factor = int(input())
count = int(input())
list_of_numbers = []
for multiplier in range(1, count + 1):
    list_of_numbers.append(factor * multiplier)
print(list_of_numbers)

# 3

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
players_sent_off = input().split()
game_was_terminated = False
for player in players_sent_off:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:  # if game_was_terminated == True:
    print("Game was terminated")

# 4

money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_digits = []
for element in money_as_string:
    money_as_digits.append(int(element))
final_sums = []
start_index = 0
while start_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(start_index, len(money_as_digits), number_of_beggars):
        sum_for_current_beggar += money_as_digits[current_index]
    final_sums.append(sum_for_current_beggar)
    start_index += 1
print(final_sums)

# 5

deck_of_cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    for card_index in range(len(right_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
    deck_of_cards = final_deck
print(final_deck)

# 8


cells = input().split("#")
amount_of_water = int(input())
total_fire = 0
total_effort = 0
fire_out_cells = []
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)
for cell in cells:
    type_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    cell_is_valid = False
    if type_of_fire == "High":
        if cell_value in high:
            cell_is_valid = True
    elif type_of_fire == "Medium":
        if cell_value in medium:
            cell_is_valid = True
    elif type_of_fire == "Low":  # else:
        if cell_value in low:
            cell_is_valid = True
    if cell_is_valid:
        if amount_of_water >= cell_value:
            amount_of_water -= cell_value
            fire_out_cells.append(cell_value)
            total_fire += cell_value
            total_effort += cell_value * 0.25
print("Cells:")
for fire_out_cell in fire_out_cells:
    print(f"- {fire_out_cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

# 9

items = input().split("|")
budget = float(input())
sell_prices = []
profit = 0
train_ticket = 150
for item in items:
    type, buying_price = item.split("->")
    buying_price = float(buying_price)
    price_is_valid = False
    if type == "Clothes":
        if buying_price <= 50.00:
            price_is_valid = True
    elif type == "Shoes":
        if buying_price <= 35.00:
            price_is_valid = True
    elif type == "Accessories":
        if buying_price <= 20.50:
            price_is_valid = True
    if price_is_valid:
        if budget >= buying_price:
            budget -= buying_price
            sell_price = buying_price * 1.40
            profit += sell_price - buying_price
            sell_prices.append(sell_price)
# Option 1
for sell_price in sell_prices:
    print(f"{sell_price:.2f}", end=" ")
print()

# Option 2
# print(" ".join([f"{sell_price:.2f}" for sell_price in sell_prices]))

# Option 3
# sell_prices_as_string = []
# for sell_price in sell_prices:
#     sell_prices_as_string.append(f"{sell_price:.2f}")
# print(" ".join(sell_prices_as_string))

print(f"Profit: {profit:.2f}")
total_income = budget + sum(sell_prices)
if total_income >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")

# 10

events = input().split("|")
total_energy = 100
total_coins = 100
factory_is_open = True
for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_value = int(event_items[1])
    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:  # order can be completed
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            factory_is_open = False
            break
if factory_is_open:  # if factory is open == True
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {type_of_event}.")

my_list = [1, 8, 4, 89, 43, 2, 132, 2, 2, "Gosho", "gosho"]

# my_list.sort(reverse=True)
# print(my_list)
#
# my_list.pop()
# print(my_list)
# my_list.pop(2)
# print(my_list)
# my_list.append(my_list.pop(2))
# print(my_list)


# my_list.insert(3, "Atanas")
# print(my_list)

# number = my_list.index(2)
# print(number)
#
# repetition = my_list.count(2)
# print(repetition)
#
# my_list.reverse()
# print(my_list)
# print(my_list[::-1])
#
# del my_list[3]
# print(my_list)
#
my_list.remove("Gosho")
print(my_list)
my_list.remove("Pesho")
print(my_list)