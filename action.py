import random


# draw a card from the deck
def draw_a_card(deck_of_cards):
    card = random.choice(deck_of_cards)
    deck_of_cards.remove(card)
    return card


# compute total score
def calculate_total_score(cards):
    total = 0
    value_set = []
    for i in cards:
        value_set.append(i[1])
    total = sum(value_set)
    ace_check = True
    while ace_check:
        if total > 21 and 11 in value_set:
            value_set.remove(11)
            value_set.append(1)
            total = sum(value_set)
        else:
            ace_check = False
    return total


# return the cards in words
def card_in_words(cards):
    hand = []
    for i in cards:
        hand.append(i[0])
    to_words = hand[0]
    for i in hand[1:]:
        to_words = to_words + ', ' + i
    return to_words
