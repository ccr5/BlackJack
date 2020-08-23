class BlackJack:

    def check_balance(self, game, obj):
        """
        :param boolean game: game status (false)
        :param Player obj: a player object
        :return boolean game:   True if obj doesn't have balance to play
        """

        if obj.balance == 0:
            print(f"{obj.name}, you haven't balance")
            game = True
            return game

    def bet(self, player, computer):
        """
        :param Player player: an object of Player class
        :param Bot computer: an object of Bot class
        :return bet_player: how much player is beting
                bet_computer: how much bot is beting
        """

        check = False
        bet_player = 0
        bet_computer = 0

        while not check:
            bet_player = int(
                input("Insert how many will you bet in this match: "))
            check = bet_player <= player.balance
            if not check:
                print("You haven't balance enough to bet this amount\n")
            else:
                pass

        player.balance -= bet_player

        if bet_player > computer.balance:
            print(
                f"{player.name}, I haven't this money, I'll give all win, right?")
            input()
            bet_computer = computer.balance
            computer.balance = 0
        else:
            bet_computer = bet_player
            computer.balance -= bet_computer

        return {'bet_player': bet_player, 'bet_computer': bet_computer}

    def check_result(self, player, computer, bets, result):
        """
        :param Player player: a player object
        :param Bot computer: a bot object
        :param list bets: a list with player and bot bet
        :param list result: the game result with who won and how much points player and bot did
        :return: all results of current game
        """

        if result[0] == 'no win':
            print("no one win, you guys have more than 21!\n")
            print(
                f"{player.name}: {result[1]} \t{computer.name}: {result[2]}")
            player.balance += bets['bet_player']
            computer.balance += bets['bet_computer']

        elif result[0] == 'draw':
            print("it's a draw O.o\n")
            print(
                f"{player.name}: {result[1]} \t{computer.name}: {result[2]}")
            player.balance += bets['bet_player']
            computer.balance += bets['bet_computer']
            player.wins += 1
            computer.wins += 1

        elif result[0] == 'h1':
            print(f"{player.name} win !!\n")
            print(
                f"{player.name}: {result[1]} \t{computer.name}: {result[2]}")
            player.balance += bets['bet_player'] + bets['bet_computer']
            player.wins += 1
            computer.defeats += 1

        elif result[0] == 'h2':
            print(f"{computer.name} win !!\n")
            print(
                f"{player.name}: {result[1]} \t{computer.name}: {result[2]}")
            computer.balance += bets['bet_player'] + bets['bet_computer']
            computer.wins += 1
            player.defeats += 1

        else:
            pass

    def check_play_again(self, choice):
        """
        :param boolean game: game status
        :return game: new game status
        """

        if choice.upper() == "Y":
            game = False
        else:
            game = True
            print("\nThanks for play")

        return game
