import random

def create_and_shuffle():
    cards_comon = list(range(0, 78))
    cards_reversed = list(range(78, 156))
    random.shuffle(cards_comon)
    random.shuffle(cards_reversed)
    n = []
    cards_up = []
    return cards_comon, cards_reversed, cards_up, n