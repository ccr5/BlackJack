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

        try:

            for x in cards.matrix:
                deck.append(x)
                deck.append(x)
                deck.append(x)
                deck.append(x)

            return deck

        except:
            print("Error: create_deck()")

    def shuffle_deck(self, deck):
        """
        :param list deck: return of create_deck function
        :return list new_deck: A shuffled deck
        """

        try:
            sequency_card = list(range(0, 52))
            r.shuffle(sequency_card)
            new_deck = []

            for x in sequency_card:
                new_deck.append(deck[x])

            return new_deck

        except:
            print("Error: shuffle_deck()")
