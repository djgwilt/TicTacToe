from Game import Game, GameError
from sys import stderr
from abc import ABC, abstractmethod
import PySimpleGUI as sg

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        pass

class Gui(Ui):
    pass
