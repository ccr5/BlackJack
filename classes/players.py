class Players:
    """
    Functions and methods to players that will play the game
    """

    def __init__(self, name, balance):
        self.name = name
        self.hand = []
        self.balance = balance
        self.wins = 0
        self.defeats = 0

    def show_info(self):
        """
        :return: how many balance, wins and defeats he has
        """

        if self.balance > 0:
            print(f"{self.name}, your balance is: {self.balance}")
        elif self.balance == 0:
            print(f"{self.name}, you haven't balance, thanks for play BlackJack")
        else:
            print(f"{self.name}, you're owe {self.balance}")

        print(f"you won {self.wins} and have {self.defeats} defeats")
