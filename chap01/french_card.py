#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple


Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades hearts clubs diamonds'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])

    from random import choice
    print(choice(deck))

    # test iterable
    for card in deck:
        print(card)

    # test slice
    print(deck[0::13])

    # if Object dosen't contain __contain__ method, then operator `in` use
    # sequential scan
    print(Card('2', 'diamonds') in deck)

    # test sorting
    for card in sorted(deck, key=spades_high):
        print(card)

