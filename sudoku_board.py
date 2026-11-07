from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, board: dict[(int, int), int]):
        self.board = board
        self.sudoku = board

        def __str__(self) -> str:
            rows = []
            for i in range(1, 10):
                row = []
                for j in range(1, 10):
                    val = self.sudoku.get((i, j), 0)
                    row.append(str(val) if val != 0 else ".")
                rows.append(" ".join(row))
            return "\n".join(rows)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        board = {}
        for atom in model.symbols(shown=True):
            row = atom.arguments[0].number
            col = atom.arguments[1].number
            val = atom.arguments[2].number

            board[(row, col)] = val


        return cls(board)
