import unittest
import bot
import cards
import dealer
import deck
import players


class TestBlackJack(unittest.TestCase):

    # Bot unittests
    def bot_play_game(self):
        npc = bot.Bot('test', 100)
        npc.hand.append(["Aces", [1, 11], "A"], ["Two", 2, "2"])
        result = npc.play_game()
        self.assertEqual(result, True)

    # Cards unittests
    def card_show_card(self):
        npc = cards.Cards()
        result = npc.show_card(["Aces", [1, 11], "A"])
        self.assertEqual(result, ["- - - -", "|     |", f"|  A  |", "|     |", "- - - -"])

    # Dealer unittests
    def dealer_check_balance(self):
        npc = dealer.Dealer()
        result = npc.check_balance(100, 200)
        self.assertEqual(result, True)

    def dealer_check_winner(self):
        npc = dealer.Dealer()
        play1 = [["Aces", [1, 11], "A"], ["Nine", 9, "9"]]
        play2 = [["Nine", 9, "9"], ["Ten", 10, "10"]]
        result = npc.check_winner(play1, play2)
        self.assertEqual(result, 'h1')

    # Deck unittests
    def deck_create_deck(self):
        npc = deck.Deck()
        result = npc.create_deck()
        self.assertEqual(len(result), 52)

    def deck_shuffle_deck(self):
        npc = deck.Deck()
        result1 = npc.create_deck()
        result2 = npc.shuffle_deck()
        self.assertEqual(len(result1), len(result2))


if __name__ == '__main__':
    unittest.main()
