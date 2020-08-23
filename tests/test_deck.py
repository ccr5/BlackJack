from classes.deck import Deck
from classes.cards import Cards


class TestDeck:

    c = Cards
    d = Deck()

    def test_create(self):
        deck = self.d.create_deck(self.c)
        assert len(deck) == 52

        for card in self.c.matrix:
            count = 0

            for other_card in deck:

                if card == other_card:
                    count += 1
                else:
                    pass

            assert count == 4

    def test_shuffle_deck(self):
        deck = self.d.create_deck(self.c)
        shuffled_deck = self.d.shuffle_deck(deck)
        assert len(shuffled_deck) == 52
        assert deck != shuffled_deck

        for card in self.c.matrix:
            count = 0

            for other_card in deck:

                if card == other_card:
                    count += 1
                else:
                    pass

            assert count == 4
