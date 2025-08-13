import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = [str(n) for n in range(2, 11)] + 'Валет Дама Король Туз'.split()
    suits = "ПИКИ БУБНЫ ТРЕФЫ ЧЕРВЫ  ".split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self.cards)
    def __getitem__(self, position):
        return self.cards[position]


if __name__ == '__main__':
    my_deck = Deck()
    print(len(my_deck))
    print(my_deck[5])
    print(choice(my_deck))
    for card in my_deck:
        print(card)