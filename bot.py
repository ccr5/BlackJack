class Bot:
    """
    Functions and methods to players that will play the game
    """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []
        self.wins = 0
        self.defeats = 0

    def welcome_message(self):
        """
        Show a welcome message when the player choose a name for him
        :return: a welcome message
        """
        print(f"Hi o/ \nMy name is {self.name} and I'll play with you")
        print("Good luck!")
        print("Aaah, I have the same balance for a fair play :)")

    def show_info(self):
        """
        Show all information about the player
        :return: how many balance, wins and defeats he has
        """
        if self.balance > 0:
            print(f"{self.name}, your balance is: {self.balance}")
        elif self.balance == 0:
            print(f"{self.name}, you haven't balance, thanks for play BlackJack")
        else:
            print(f"{self.name}, you're owe {self.balance}")

        print(f"you won {self.wins} and have {self.defeats} defeats")

    def play_game(self):
        """
        This Function will see if he needs one more card or not
        :return: True if he needs one more card and False to not
        """
        sum_hand = 0
        count_a = 0

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

            if sum_hand < 21:
                return True
            else:
                return False
