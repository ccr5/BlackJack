import random as r
from deck import Deck
from cards import Cards


class Dealer:
    """
    Main methods and functions to play BlackJack
    """

    @staticmethod
    def check_balance(bet, balance):
        """
        Check if player or bot can make a bet
        :param bet: how many they wanna bet
        :param balance: balance to check
        :return: True if can pay or not
        """

        if bet <= balance:
            return True
        else:
            return False

    @staticmethod
    def check_winner(hand1, hand2):
        """
        This function figure out how win the game
        :param hand1: player hand
        :param hand2: bot hand
        :return: the name who won
        """
        h1 = 0
        h2 = 0
        count_a_h1 = 0
        count_a_h2 = 0

        for card in hand1:
            if card[2] == 'A':
                count_a_h1 += 1
            else:
                h1 += card[1]

        for card in hand2:
            if card[2] == 'A':
                count_a_h2 += 1
            else:
                h2 += card[1]

        if count_a_h1 >= 1 and h1 > 10:
            h1 += 1 * count_a_h1
        elif count_a_h1 == 1 and h1 <= 10:
            h1 += 11
        else:
            pass

        if count_a_h2 >= 1 and h2 > 10:
            h2 += 1 * count_a_h2
        elif count_a_h2 == 1 and h2 <= 10:
            h2 += 11
        else:
            pass

        if h1 > 21 and h2 > 21:
            return 'no win', h1, h2
        elif h1 <= 21 and h2 > 21:
            return 'h1', h1, h2
        elif h1 > 21 and h2 <= 21:
            return 'h2', h1, h2
        elif h1 == 21 and h2 == 21:
            return 'draw', h1, h2
        elif h1 == 21:
            return 'h1', h1, h2
        elif h2 == 21:
            return 'h2', h1, h2
        elif h1 > h2:
            return 'h1', h1, h2
        elif h2 > h1:
            return 'h2', h1, h2
        else:
            pass
