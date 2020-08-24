import os
from classes.humans import RealPlayer
from classes.bot import Bot
from classes.blackjack import BlackJack
from classes.deck import Deck
from classes.dealer import Dealer
from classes.cards import Cards


def main():
    """ main method of blackjack game """

    os.system('clear') or None
    print("Welcome to BlackJack -_- \n")

    name = input("First, What is your name? ")
    balance = int(input("How many money have you today? "))
    player = RealPlayer(name, balance)

    bot = input("Could you choose a name for a bot? ")
    computer = Bot(bot, balance)
    os.system('clear') or None
    computer.welcome_message()

    input("\nSo let's play? ")
    os.system('clear') or None

    card = Cards()
    dealer = Dealer()
    deck = Deck()
    bj = BlackJack()

    game = False

    while not game:

        player.hand = []
        computer.hand = []
        game_deck = deck.shuffle_deck(deck.create_deck(card))
        os.system('clear') or None

        bj.check_balance(game, player)
        if game == True:
            break

        bj.check_balance(game, computer)
        if game == True:
            break

        os.system('clear') or None
        ask_player = False

        bets = bj.bet(player, computer)

        while not ask_player:

            if len(player.hand) == 0:
                print("You don't have any card in your hand")
            else:
                hand = card.show_card(player.hand)
                for c in hand:
                    for x in c:
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

        result = dealer.check_winner(
            player.hand, computer.hand)

        bj.check_result(player, computer, bets, result)

        player.show_info()
        hand = card.show_card(player.hand)
        for c in hand:
            for x in c:
                print(x)

        print("\n")

        computer.show_info()

        hand = card.show_card(computer.hand)
        for c in hand:
            for x in c:
                print(x)

        print("\n")

        choice = input("Do you wanna play again (Y/N): ")
        choice = choice.upper()

        game = bj.check_play_again(choice)


if __name__ == '__main__':
    main()
