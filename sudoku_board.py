from typing import Tuple
import clingo


class board:
    def __init__(self, board: dict[(int, int), int]):
        self.board = board

    def __str__(self) -> str:
         s = ""
         for i in range(1, 10):
            for j in range(1, 10):
                s += str(self.board[(i, j)])
            s += "\n"
         return s

    @classmethod
    def from_str(cls, s: str) -> "board":
        board = {}
        rows = [row.strip() for row in s.strip().splitlines()]

        for i, row in enumerate(rows, start=1):
            for j, value in enumerate(row, start=1):
                board[(i, j)] = int(value)
        return cls(board)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "board":
        board = {}
        for atom in model.symbols(shown=True):
            if atom.name == "board":
                row = atom.arguments[0].number
                col = atom.arguments[1].number
                val = atom.arguments[2].number

                board[(row, col)] = val
        return cls(board)
