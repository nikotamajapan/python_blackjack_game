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
import time
from time import sleep


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

        return print(self.value)

    def is_blackjack(self):
        return self.calc_value() == 21

    
deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand(dealer=True)

player_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())

player_hand.calc_value()
dealer_hand.calc_value()
