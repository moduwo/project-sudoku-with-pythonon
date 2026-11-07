import sys
import clingo


class SudokuApp(clingo.Application):
    program_name = "sudoku"

    def main(self, control, files):
        control.load("sudoku.lp")

        for f in files:
            control.load(f)

        control.ground([("base", [])])
        control.solve()


if __name__ == "__main__":
    app = SudokuApp()
    clingo.clingo_main(app, sys.argv[1:])