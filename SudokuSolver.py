class SudokuSolver:
    def __init__(self):
        """
        Initializes a new instance of the SudokuSolver class.
        """
        self.grid = {}

    def list_to_dict(self, puzzle: list) -> dict:
        """
        Converts a list representation of a Sudoku puzzle to a dictionary representation.

        Args:
            puzzle (list): A 9x9 list representing a Sudoku puzzle.

        Returns:
            dict: A dictionary representation of the Sudoku puzzle.
        """
        for i in range(9):
            for j in range(9):
                self.grid[(i, j)] = puzzle[i][j]
        return self.grid

    def dict_to_list(self, grid: dict) -> list:
        """
        Converts a dictionary representation of a Sudoku puzzle to a list representation.

        Args:
            grid (dict): A dictionary representation of a Sudoku puzzle.

        Returns:
            list: A 9x9 list representing the Sudoku puzzle.
        """
        puzzle = [[0 for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                puzzle[i][j] = grid[(i, j)]
        return puzzle

    def get_column(self, column: int, grid: dict) -> list:
        """
        Gets a column from a dictionary representation of a Sudoku puzzle.

        Args:
            column (int): The index of the column to get.
            grid (dict): A dictionary representation of a Sudoku puzzle.

        Returns:
            list: A list representing the column.
        """
        return [grid[(i, column)] for i in range(9)]

    def get_row(self, row: int, grid: dict) -> list:
        """
        Gets a row from a dictionary representation of a Sudoku puzzle.

        Args:
            row (int): The index of the row to get.
            grid (dict): A dictionary representation of a Sudoku puzzle.

        Returns:
            list: A list representing the row.
        """
        return [grid[(row, j)] for j in range(9)]

    def get_box(self, row: int, column: int, grid: dict) -> list:
        """
        Gets a box from a dictionary representation of a Sudoku puzzle.

        Args:
            row (int): The index of the row containing the box.
            column (int): The index of the column containing the box.
            grid (dict): A dictionary representation of a Sudoku puzzle.

        Returns:
            list: A list representing the box.
        """
        box_row = (row // 3) * 3
        box_col = (column // 3) * 3
        return [grid[(i, j)] for i in range(box_row, box_row+3)
                for j in range(box_col, box_col+3)]

    def print_sudoku_and_solution(self, orginal: list, solved: dict):
        """
        Prints the original and solved Sudoku puzzles side by side.

        Args:
            orginal (list): A 9x9 list representing the original Sudoku puzzle.
            solved (dict): A dictionary representation of the solved Sudoku puzzle.
        """
        print("Orginal: \t\t\t Solved:")
        for i in range(9):
            o_row = orginal[i]
            s_row = [solved[(i, j)] for j in range(9)]
            print(f"{o_row}\t{s_row}")

    def solve(self, puzzle: list) -> list:
        """
        Solves a Sudoku puzzle.

        Args:
            puzzle (list): A 9x9 list representing a Sudoku puzzle.

        Returns:
            list: A 9x9 list representing the solved Sudoku puzzle.
        """
        orginal = [row[:] for row in puzzle]
        self.list_to_dict(puzzle)
        unsolved = True
        numbers = set([n for n in range(0, 10)])
        while unsolved:
            # find least possiblities
            taken = 0
            values = {}
            pos_x = 0
            pos_y = 0
            for x in range(9):
                for y in range(9):
                    n = self.grid[(x, y)]
                    if n == 0:  # its unasigned
                        column = self.get_column(y, self.grid)
                        row = self.get_row(x, self.grid)
                        box = self.get_box(x, y, self.grid)

                        asigned_values = set(column + row + box)

                        if (len(asigned_values) > taken):
                            values = asigned_values
                            taken = len(asigned_values)
                            pos_x = x
                            pos_y = y

            if (taken == 0 or taken == 10):
                unsolved = False
                break
            n = (numbers - values).pop()
            self.grid[(pos_x, pos_y)] = n
        self.print_sudoku_and_solution(orginal, self.grid)
        return self.dict_to_list(self.grid)
