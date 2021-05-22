# from blackjack import deal
import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4


def deal():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 1:
            card = "A"
        hand.append(card)
    return hand

# deal()
# print(hand)


def hit(hand):
    # for i in range(2):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 1:
        card = "A"
    hand.append(card)
    return hand


def total(hand):
    score = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score += 10
        elif card == "A":
            if score >= 11:
                score = score + 1
            else:
                score += 11
        else:
            score += card
    return score


def play_again():
    aaa = input("y?")
    if aaa == "y":
        return
    else:
        print("finish")
        exit()


def result(dealer_hand, player_hand):
    if total(player_hand) > total(dealer_hand):
        print(f"dealer {total(dealer_hand)} / you {total(player_hand)} WIN !")
    elif total(player_hand) < total(dealer_hand):
        print(f"dealer {total(dealer_hand)} / you {total(player_hand)} lose ...")


def game():
    dealer_hand = deal()
    player_hand = deal()
    print(f"dealer_hand -> {dealer_hand[0]}")
    print(f"player_hand -> {player_hand} >> {total(player_hand)}")
    
    choice = 0

    while choice != quit:
        choice = input("hit or stand :").lower()
        if choice == "hit":
            hit(player_hand)
            print(f" your {player_hand[-1]} add to {player_hand} total {total(player_hand)} ")
            if total(player_hand) > 21:
                print("over 21 you lose ...")
                choice = quit
        elif choice == "stand":
            print(f" dealer-2 {dealer_hand[1]} total {total(dealer_hand)} ")
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(f" dealer {dealer_hand[-1]} add to {dealer_hand} total {total(dealer_hand)} ")
                if total(dealer_hand) > 21:
                    print("over 21 you WIN !")
                    choice = quit
            
            result()
            choice = quit


game()

