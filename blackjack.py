# blackjack
# Game
    # Consists of n players, 1 dealer and n - 1 players
    # Consists of one deck of 52 Cards
    # Each player dealt 2 Cards and can hit or stay
    # Dealer is dealt one card shown and one hidden
    # Players ante chips each round
    # if players win they 2x their money, if not they lose

import random

class BlackJack:
    def __init__(self):
        self.players = []
        self.Dealer = None

    def __init_game(self, num_players):
        for i in range(num_players-1):
            self.players.append(Player(i))
        self.Dealer = Dealer()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = None

class Dealer:
    def __init__(self):
        self.hand = None

    def deal_hands(self):
        pass

class Deck:
    def __init__(self):
        self.deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4

    def get_card(self):
        random_number = random.randint(0, len(self.deck))
        self.deck[random_number], self.deck[-1] = self.deck[-1], self.deck[random_number]
        return self.deck.popleft()


class Ante:
    def __init__(self):
        self.amount = 0

    def raise_ante(self, amount):
        self.amount += amount
        return self.amount

class Hand:
    pass

class Round:
    def __init__(self) -> None:
        self.