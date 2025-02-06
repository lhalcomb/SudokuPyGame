from itertools import chain, product
from SudokuPyGame import load_sudoku

grid = load_sudoku('sudoku.csv')

possibilities = [
        (r, c, n)
        for r, c in product(range(9), range(9))
        for n in (range(9) if grid[r][c] == 0 else (grid[r][c] - 1,))
    ]

# for r, c, n in possibilities:
#     print(r, c, n)