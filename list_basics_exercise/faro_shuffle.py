cards_deck = input().split()
number_of_shuffles = int(input())
deck_half = len(cards_deck) // 2

for shuffle in range(number_of_shuffles):
    final_deck = []
    left_half_deck = cards_deck[0:deck_half]
    right_half_deck = cards_deck[deck_half:]
    for card_index in range(len(left_half_deck)):
        final_deck.append(left_half_deck[card_index])
        final_deck.append(right_half_deck[card_index])
    cards_deck = final_deck
print(final_deck)
