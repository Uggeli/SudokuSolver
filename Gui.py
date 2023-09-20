import tkinter as tk
from SudokuSolver import SudokuSolver

from puzzles import sudoku  # for placeholder puzzle


class SudokuSolverGui:
    def __init__(self, solver: SudokuSolver):
        self.solver: SudokuSolver = solver
        self.root = tk.Tk()
        self.root.title("Sudoku Solver")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(background="white")

        # Create a frame for the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, pady=10)

        # Create the "Select Puzzle Area" button
        select_button = tk.Button(button_frame, text="Select Puzzle Area", command=self.select_area)
        select_button.pack(side=tk.LEFT, padx=10)

        # Create the "Solve" button
        solve_button = tk.Button(button_frame, text="Solve", command=self.solve)
        solve_button.pack(side=tk.LEFT, padx=10)

        grid_frame = tk.Frame(self.root)
        grid_frame.pack(side=tk.TOP, pady=10)

        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = tk.Entry(grid_frame, width=3, font=("Arial", 16))
                cell.grid(row=i, column=j, padx=2, pady=2)
                row.append(cell)
            self.cells.append(row)

        self.root.mainloop()

    def populate_puzzle_grid(self, puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    self.cells[i][j].insert(0, str(puzzle[i][j]))

    def clear_puzzle_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)

    def select_area(self):
        # placeholder
        self.puzzle = sudoku
        self.clear_puzzle_grid()
        self.populate_puzzle_grid(self.puzzle)

    def solve(self):
        if not hasattr(self, "puzzle"):
            return
        solved = self.solver.solve(self.puzzle)
        if solved:
            self.clear_puzzle_grid()
            self.populate_puzzle_grid(solved)

