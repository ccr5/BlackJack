from classes.dealer import Dealer
from classes.cards import Cards


class TestDealer():

    d = Dealer()
    c = Cards()

    def test_check_winner(self):
        hand_1 = [self.c.matrix[0], self.c.matrix[9]]
        hand_2 = [self.c.matrix[0], self.c.matrix[7]]
        assert self.d.check_winner(hand_1, hand_2) == ('h1', 21, 19)

        hand_1 = [self.c.matrix[0], self.c.matrix[7]]
        hand_2 = [self.c.matrix[0], self.c.matrix[7]]
        assert self.d.check_winner(hand_1, hand_2) == ('draw', 19, 19)

        hand_1 = [self.c.matrix[0], self.c.matrix[7]]
        hand_2 = [self.c.matrix[9], self.c.matrix[7], self.c.matrix[9]]
        assert self.d.check_winner(hand_1, hand_2) == ('h1', 19, 28)

        hand_1 = [self.c.matrix[9], self.c.matrix[7], self.c.matrix[9]]
        hand_2 = [self.c.matrix[9], self.c.matrix[7], self.c.matrix[9]]
        assert self.d.check_winner(hand_1, hand_2) == ('no win', 28, 28)
