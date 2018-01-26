import collections

# 构建 Card 类表示一张纸牌
Card = collections.namedtuple("Card", ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '黑桃 红桃 梅花 方片'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]


suit_values = {'黑桃': 3, '红桃': 2, '方片': 1, '梅花': 0}


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

deck = FrenchDeck()
for card in sorted(deck, key=spades_high):
    print(card)
