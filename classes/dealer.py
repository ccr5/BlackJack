class Dealer:
    """
    Main methods and functions to play BlackJack
    """

    def check_As(self, count_A, sum):
        if count_A >= 1 and sum > 10:
            sum += 1 * count_A
        elif count_A == 1 and sum <= 10:
            sum += 11
        else:
            pass

        return sum

    def check_winner(self, hand1, hand2):
        """
        :param list hand1: player hand
        :param list hand2: bot hand
        :return tuple:  result: str
                        hand1 points: int
                        hand2 points: int
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

        h1 = self.check_As(count_a_h1, h1)
        h2 = self.check_As(count_a_h2, h2)

        if h1 > 21 and h2 > 21:
            return 'no win', h1, h2
        elif h1 <= 21 and h2 > 21:
            return 'h1', h1, h2
        elif h1 > 21 and h2 <= 21:
            return 'h2', h1, h2
        elif h1 == h2:
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
