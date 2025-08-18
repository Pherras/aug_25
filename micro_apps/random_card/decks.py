from collections import namedtuple
from random import shuffle

from micro_apps.random_card.settings import deck_36

Card = namedtuple('Card', ['suit', 'rank'])

class Deck:

    ranks_36 = [str(i) for i in range(6,11)] + list('ВДКТ')
    ranks_52 = [str(i) for i in range(2,11)] + list('ВДКТ')

    suits = ['♠', '♥', '♦', '♣']


    def __init__(self, type_of_deck: str = deck_36):
        match type_of_deck:
            case "36 карт": self._data = [Card(suit, rank) for suit in self.suits for rank in self.ranks_36]
            case "52 карты": self._data = [Card(suit, rank) for suit in self.suits for rank in self.ranks_52]
            case _: raise ValueError("Неверный тип колоды")
        self._last_card = None
        shuffle(self._data)

    def get_card(self):
        if len(self._data) > 0:
            self._last_card = self._data.pop()
            return self._last_card
        else: return self._last_card

    def __len__(self):
        return len(self._data)

    def __getitem__(self, position):
        return self._data[position]

