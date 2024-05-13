from Game import Game, GameError
from sys import stderr
from abc import ABC, abstractmethod
#import PySimpleGUI as sg

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while self._game.winner is None:
            print(self._game)
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                self._game.play(row,col)
            except GameError as e:
                print(e,file=stderr)
        print("The winner was",self._game.winner)

class Gui(Ui):
    pass
