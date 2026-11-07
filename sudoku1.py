import sys
from xml.parsers.expat import model
import clingo


class SudokuApp(clingo.Application):
    program_name = "sudoku"

    def main(self, control, files):
        control.load("sudoku.lp")

        for f in files:
            control.load(f)

        control.ground([("base", [])])
        control.solve()

    def print_model(self, model, printer):
        for atom in sorted(model.symbols(shown=True), key=str):
            print(atom, end=" ")
        print()

if __name__ == "__main__":
    app = SudokuApp()
    clingo.clingo_main(app, sys.argv[1:])