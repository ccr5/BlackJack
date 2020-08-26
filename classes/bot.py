from classes.players import Players


class Bot(Players):
    """
    Functions and methods to players that will play the game
    """

    def welcome_message(self):
        """
        :return: a welcome message
        """
        print(f"Hi o/ \nMy name is {self.name} and I'll play with you")
        print("Good luck!")
        print("Aaah, I have the same balance for a fair play :)")

    def play_game(self):
        """
        :return boolean:    True if he needs more cards 
                            False if he don't need more cards
        """

        sum_hand = 0
        count_a = 0

        try:
            if len(self.hand) == 0:
                return True
            else:
                for card in self.hand:
                    if card[2] == 'A':
                        count_a += 1
                        if count_a >= 1 and sum_hand > 10:
                            sum_hand += 1 * count_a
                        elif count_a == 1 and sum_hand <= 10:
                            sum_hand += 11
                        else:
                            pass
                    else:
                        sum_hand += card[1]

            return True if sum_hand < 21 else False

        except:
            print("Error: play_game()")
