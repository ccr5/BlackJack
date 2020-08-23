import random as r


class Deck:
    """
    Function and methods about deck
    """

    def create_deck(self, cards):
        """
        :param Cards cards: a card object
        :return list deck: A sort deck to play
        """

        deck = []

        for x in cards.matrix:
            deck.append(x)
            deck.append(x)
            deck.append(x)
            deck.append(x)

        return deck

    def shuffle_deck(self, deck):
        """
        :param list deck: return of create_deck function
        :return list new_deck: A shuffled deck
        """

        sequency_card = list(range(0, 52))
        r.shuffle(sequency_card)
        new_deck = []

        for x in sequency_card:
            new_deck.append(deck[x])

        return new_deck
