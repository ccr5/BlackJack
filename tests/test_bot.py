from classes.bot import Bot
from classes.cards import Cards


class TestBot:

    def test_play_game(self):
        b = Bot('test', 100)
        c = Cards()

        b.hand = [c.matrix[0], c.matrix[9]]
        assert b.play_game() == False

        b.hand = [c.matrix[0], c.matrix[5]]
        assert b.play_game() == True
