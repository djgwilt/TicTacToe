from Ui import Ui
from Game import Game, GameError
from sys import stderr

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        pass


