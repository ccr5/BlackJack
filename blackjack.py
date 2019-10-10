import os
from players import Players
from bot import Bot
from dealer import Dealer
from cards import Cards
from deck import Deck


class BlackJack:
    """
    Main class
    """
    global bet_player, bet_computer
    global check

    os.system('clear') or None
    print("Welcome to BlackJack -_- \n")

    name = input("First, What is your name? ")
    balance = int(input("How many money have you today? "))
    player = Players(name, balance)

    bot = input("Could you choose a name for a bot? ")
    computer = Bot(bot, balance)
    os.system('clear') or None
    computer.welcome_message()

    start = input("\nSo let's play? ")
    os.system('clear') or None

    deck = Deck()
    dealer = Dealer()
    cards = Cards()

    game = False

    while not game:

        bet_player = 0
        bet_computer = 0
        player.hand = []
        computer.hand = []
        game_deck = deck.shuffle_deck()
        os.system('clear') or None

        if player.balance == 0:
            print(f"{player.name}, you haven't balance")
            game = True
            break
        elif computer.balance == 0:
            print(f"{computer.name}, you haven't balance")
            game = True
            break

        check = False

        while not check:
            bet_player = int(input("Insert how many will you bet in this match: "))
            check = dealer.check_balance(bet_player, player.balance)
            if not check:
                print("You haven't balance enough to bet this amount\n")
            else:
                pass

        player.balance -= bet_player

        if bet_player > computer.balance:
            print(f"{player.name}, I haven't this money, I'll give all win, right?")
            input()
            bet_computer = computer.balance
            computer.balance = 0
        else:
            bet_computer = bet_player
            computer.balance -= bet_computer

        os.system('clear') or None
        ask_player = False

        while not ask_player:

            if len(player.hand) == 0:
                print("You don't have any card in your hand")
            else:
                hand = cards.show_card(player.hand)
                for card in hand:
                    for x in card:
                        print(x)

            i = input('Would you like one more card? ')
            i = i.upper()

            if i == 'Y':
                player.hand.append(game_deck.pop())
                ask_player = False
            else:
                ask_player = True

        os.system('clear') or None
        bot_player = False

        while not bot_player:

            i = computer.play_game()
            if i is True:
                computer.hand.append(game_deck.pop())
            else:
                bot_player = True

        result = dealer.check_winner(player.hand, computer.hand)

        if result[0] == 'no win':
            print("no one win, you guys have more than 21!\n")
            print(f"{player.name}: {result[1]} \t{computer.name}: {result[2]}")
            player.balance += bet_player
            computer.balance += bet_computer
        elif result[0] == 'draw':
            print("it's a draw O.o\n")
            print(f"{player.name}: {result[1]} \t{computer.name}: {result[2]}")
            player.balance += bet_player
            computer.balance += bet_computer
            player.wins += 1
            computer.wins += 1
        elif result[0] == 'h1':
            print(f"{player.name} win !!\n")
            print(f"{player.name}: {result[1]} \t{computer.name}: {result[2]}")
            player.balance += bet_player + bet_computer
            player.wins += 1
            computer.defeats += 1
        elif result[0] == 'h2':
            print(f"{computer.name} win !!\n")
            print(f"{player.name}: {result[1]} \t{computer.name}: {result[2]}")
            computer.balance += bet_player + bet_computer
            computer.wins += 1
            player.defeats += 1
        else:
            pass

        player.show_info()
        hand = cards.show_card(player.hand)
        for card in hand:
            for x in card:
                print(x)
        print("\n")
        computer.show_info()
        hand = cards.show_card(computer.hand)
        for card in hand:
            for x in card:
                print(x)
        print("\n")

        choice = input("Do you wanna play again (Y/N): ")
        choice = choice.upper()

        if choice == "Y":
            game = False
        else:
            game = True

    print("\nThanks for play")
