import random as r
from cards import Cards


class Deck:
    """
    Function and methods about deck
    """

    def __init__(self):
        self.cards = Cards.matrix
        self.deck = Deck.create_deck(self)

    def create_deck(self):
        """
        Creating a deck to play BlackJack
        :return: A sort deck to play
        """

        deck = []

        for x in self.cards:
            deck.append(x)
            deck.append(x)
            deck.append(x)
            deck.append(x)

        return deck

    def shuffle_deck(self):
        """
        Shuffle a deck
        :return: A shuffle deck
        """
        sequency_card = list(range(0, 52))
        r.shuffle(sequency_card)
        new_deck = []
        for x in sequency_card:
            new_deck.append(self.deck[x])

        return new_deck
