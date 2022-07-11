from models.player import Player
import random

class Game:
    def __init__(self):
        self.rules = {
            'rock':'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
        self.choices = ['rock', 'paper', 'scissors']

    def generate_player(self):
        return Player('Computer', random.choice(self.choices))

    def play_game(self, player_1, player_2):
        winning_player = None
        if player_2.choice == self.rules[player_1.choice]:
            winning_player = player_1
        elif player_1.choice == self.rules[player_2.choice]:
            winning_player = player_2

        return winning_player
