from classes.blackjack import BlackJack
from classes.players import Players


class TestBlackjack:

    b = BlackJack()
    p = Players('test', 0)

    def test_check_play_again(self):

        choice = 'y'
        assert self.b.check_play_again(choice) == False

        choice = 'n'
        assert self.b.check_play_again(choice) == True

    def test_check_balance(self):

        game = False
        assert self.b.check_balance(game, self.p) == True
