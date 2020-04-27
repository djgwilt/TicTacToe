from tkinter import Button, Tk, Toplevel, Frame, N,S,E,W,X,Y, LEFT,RIGHT, END, Scrollbar, Text, Message, Grid, StringVar
from Game import Game, GameError
from sys import stderr
from itertools import product
from abc import ABC, abstractmethod

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe")
        self._game_win = None
        frame = Frame(root)
        frame.pack(fill=X)

        Button(
            frame,
            text='Show Help',
            command=self.help_callback
        ).pack(fill=X)

        Button(
            frame,
            text='Play Game',
            command=self.play_callback
        ).pack(fill=X)

        Button(
            frame,
            text='Quit',
            command=root.quit
        ).pack(fill=X)

        console = Text(frame, height=4, width=50)
        scroll = Scrollbar(frame)
        scroll.pack(side=RIGHT, fill=Y)
        console.pack(side=LEFT, fill=Y)

        scroll.config(command=console.yview)
        console.config(yscrollcommand=scroll.set)

        self._console = console
        self._root = root

    def help_callback(self):
        pass

    def _game_close(self):
        self._game_win.destroy()
        self._game_win = None

    def play_callback(self):
        if self._game_win:
            return

        self._game = Game()
        self._finished = False

        game_win = Toplevel(self._root)
        self._game_win = game_win

        game_win.title("Game")
        Grid.rowconfigure(game_win,0,weight=1)
        Grid.columnconfigure(game_win,0,weight=1)
        
        frame = Frame(game_win)
        frame.grid(row=0,column=0,sticky=N+S+E+W)

        dim = Game._DIM
        self._buttons = [[None for _ in range(dim)] for _ in range(dim)]

        for row,col in product(range(dim),range(dim)):
            b = StringVar()
            b.set(self._game.at(row+1,col+1))

            cmd = lambda r=row,c=col : self.play_and_refresh(r,c)

            Button(
                frame,
                textvariable=b,
                command=cmd
            ).grid(row=row,column=col,sticky=N+S+E+W)

            self._buttons[row][col] = b

        for i in range(dim):
            Grid.rowconfigure(frame,i,weight=1)
            Grid.columnconfigure(frame,i,weight=1)

        Button(game_win, text="Dismiss", command=self._game_close).grid(row=1,column=0)

    def play_and_refresh(self,row,col):
        try:
            self._game.play(row+1,col+1)
        except GameError as e:
            self._console.insert(END, f"{e}\n")

        text = self._game.at(row+1,col+1)
        self._buttons[row][col].set(text)

        w = self._game.winner
        if w is not None:
            if w is Game.DRAW:
                self._console.insert(END, "The game was drawn\n")
            else:
                self._console.insert(END,f"The winner was {w}\n")

    def run(self):
        self._root.mainloop()

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while not self._game.winner:
            while True:
                print(self._game)
                try:
                    row = int(input("Which row? "))
                    col = int(input("Which column? "))
                except ValueError:
                    print(f"Row and Column should be numbers in the range 1-{self._game._DIM}.")
                    continue
                try:
                    self._game.play(row,col)
                    break
                except GameError as e:
                    print(f"Game error {e}",file=stderr)

        print(self._game)
        w = self._game.winner
        if w is Game.DRAW:
            print("The game was drawn")
        else:
            print(f"The winner was {w}")
