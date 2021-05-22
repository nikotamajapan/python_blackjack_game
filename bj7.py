# ぐーれ
# ? オブジェクト指向プログラミング
# * Object
# * Oriented
# * Programming


# ? プログラミング的思考
#   (class Card) トランプ（suit=柄, number=数字)
#   (class Deck) デッキ (deal=カードを配る, shuffle)
#   (class Hand) 手札
#  __init__
#  player, dealer
#  cards
#  value
#  hit(add_card)
#  total(calc_value)
#  is_blackjack()
#  show()
#  (class Game) ゲーム


import random
# import time
# from time import sleep


class Card():

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return f'{self.suit} {self.number}'


class Deck():

    def __init__(self):
        suits = ['♠', '♥', '♣', '♦']
        numbers = [
            {'key': 'A', 'value': 11},
            {'key': '2', 'value': 2},
            {'key': '3', 'value': 3},
            {'key': '4', 'value': 4},
            {'key': '5', 'value': 5},
            {'key': '6', 'value': 6},
            {'key': '7', 'value': 7},
            {'key': '8', 'value': 8},
            {'key': '9', 'value': 9},
            {'key': '10', 'value': 10},
            {'key': 'J', 'value': 10},
            {'key': 'Q', 'value': 10},
            {'key': 'K', 'value': 10},
        ]

        self.cards = []

        for suit in suits:
            for number in numbers:
                self.cards.append(Card(suit, number))

    def deal(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)


class Hand():

    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.total = 0

    def add_card(self, card):
        self.cards.append(card)

    def calc_value(self):
        self.value = 0
        ace = False
        for card in self.cards:
            self.value += int(card.number['value'])
            if card.number['key'] == 'A':
                ace = True

        if ace and self.value > 21:
            self.value -= 10

        return self.value

    def is_blackjack(self):
        return self.calc_value() == 21

    def show(self, show_two_cards=False):
        if self.dealer is True:
            print('Dealer hand:')
        else:
            print('your hand:')
        # print(f"{'Dealer' if self.dealer else 'Your'} hand:")
        # ? <true> if <condition> else <false>

        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_two_cards and not self.is_blackjack():
                pass
            else:
                print(f"{card.suit}{card.number['key']}")
        if not self.dealer:
            print('Total:', self.calc_value())
        print()


class Game():
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.calc_value() > 21:
                print('あなたは21を超えました. Dealer wins!')
                return True
            elif dealer_hand.calc_value() > 21:
                print('ディーラーは21を超えました. You win!')
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print('ふたりともブラックジャックです. Draw!')
                return True
            elif player_hand.is_blackjack():
                print('あなたはブラックジャックです! You win!')
                return True
            elif dealer_hand.is_blackjack():
                print('ディーラーはブラックジャックです! Dealer wins!')
                return True
        else:
            if player_hand.calc_value() > dealer_hand.calc_value():
                print('あなたの勝ちです!')
            elif player_hand.calc_value() == dealer_hand.calc_value():
                print('引き分けです!')
            else:
                print('残念、ディーラーの勝ちです‥')
            return True
        return False        

    def play(self):
        game_to_play = 0
        game_number = 0

        while game_to_play <= 0:
            try:
                game_to_play = int(input('how many time ? ')) 
            except ValueError:
                print('how many ??? ')

        while game_number < game_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())

            print()
            print(f"game_number {game_number} / {game_to_play}")
            print()

            player_hand.show()
            dealer_hand.show()

            if self.check_winner(player_hand, dealer_hand):
                continue
            
            print('1 hit or stand')

            if self.check_winner(player_hand, dealer_hand):
                continue
            print('2 draw card until 17')
            if self.check_winner(player_hand, dealer_hand, game_over=True):
                continue
            print('3 result ')

            self.check_winner(player_hand, dealer_hand, game_over=True)


game = Game()                
game.play()


