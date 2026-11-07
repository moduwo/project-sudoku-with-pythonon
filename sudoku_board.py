from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, board: dict[(Tuple[int, int], int)]):
        self.board = board
        self.sudoku = board

    def __str__(self) -> str:
        s = ""
        for row in range(1, 10):
            for col in range(1, 10):
                s += str(self.board.get((row, col)))

                if col < 9:
                    if col % 3 == 0:
                        s += "  "
                    else:
                        s += " "

            s += "\n"

            if row % 3 == 0 and row < 9:
                s += "\n"
            
        return s

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        board = {}
        for atom in model.symbols(shown=True):
            row = atom.arguments[0].number
            col = atom.arguments[1].number
            val = atom.arguments[2].number

            board[(row, col)] = val


        return cls(board)
