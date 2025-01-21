"""
Sudoku Project built in pygame for algorithms to solve sudoku puzzles

Algorithms Used:
- Backtracking Algorithms: DFS, Dancing Links

"""

import pygame
import pandas as pd
import numpy as np
import sys
import time
import random
from DrawSudoku import drawSudoku
from DLX import DLX, Node



#CONSTANTS

""" Colors """
white = (255, 255, 255)
black = (0, 0, 0)
size = 1080
cellSize = size / 9

#PYGAME INITIALIZATION
def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Sudoku Solver")
    font = pygame.font.SysFont(None, 40)
    return screen, font

#Sudoku Randomized Grid Selection Using NumPy and Pandas
def load_sudoku(file_path) -> list[list[int]]:
    df = pd.read_csv(file_path)
    random_quiz = random.choice(df['quizzes'])
    grid = np.array([int(char) for char in random_quiz]).reshape(9, 9)
    return grid


#Helper tooll used in dfs logic
def is_valid(grid, num, pos: tuple):
        row, col = pos #tuple of row and column pair
        #check the row
        if num in grid[row]:
            return False
        #check the column
        if num in grid[:, col]:
            return False
        
        box_x, box_y = col // 3, row // 3 
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if grid[i][j] == num and (i, j) != pos:
                    return False
                
        return True

#DFS Backtracking solvler with visualization implemented
def dfs_backtracking_solver(grid, screen, font, draw):
    
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, num, (row, col)):
                        grid[row][col] = num
                        screen.fill(white)
                        draw.drawGrid(screen, size)
                        draw.draw_numbers(screen, font, grid)
                        pygame.display.flip()
                        if dfs_backtracking_solver(grid, screen, font, draw):
                            return True
                        grid[row][col] = 0
                        screen.fill(white)
                        draw.drawGrid(screen,size)
                        draw.draw_numbers(screen, font, grid)
                        pygame.display.flip()

                return False
    return True


"""Dancing Links Implementation"""
def build_cover_matrix(grid):
    dlx = DLX()
    for row in range(9):
        for col in range(9):
            for digit in range(1, 10):
                #print(f"row: {row}, col: {col}, grid size: {len(grid)}x{len(grid[0])}")
                if grid[row][col] != 0 and grid[row][col] != digit:
                    continue #skip the invalid digit placements
                
                cell_col = 9 * row + col
                row_col = 81 + 9 * row + digit - 1
                col_col = 162 + 9 * col + digit - 1
                box = (row// 3) * 3 + col // 3
                box_col = 243 + 9 * box + digit - 1

                for constraint_col in [cell_col, row_col, col_col, box_col]:
                    if constraint_col is None:
                        raise ValueError(f"Invalid column: {constraint_col}")
                    dlx.add_node(row=f"{row}{col}{digit}", col = constraint_col)
    return dlx

#Solve the sudoku using the dancing links algorithm
def solve_sudoku_dlx(grid, screen, font, draw):
    dlx = build_cover_matrix(grid)
    
    solution = []
    def search(k):
        if dlx.head.right == dlx.head:
            return True # We did it, it is solved
        
        #Select the column with the fewest rows
        col = min(
            (node for node in dlx.iterate(dlx.head.right, "right")),
            key= lambda x : sum(1 for _ in dlx.iterate(x.down, "down")), #count the number of rows
        )
        dlx.cover(col)
        for row_node in dlx.iterate(col.down, "down"):
            solution.append(row_node)
            for col_node in dlx.iterate(row_node.right, "right"):
                dlx.cover(col_node)

            if search(k + 1):
                return True
            
            #backtrack
            solution.pop()
            for col_node in dlx.iterate(row_node.right, "right"):
                dlx.uncover(col_node)
        dlx.uncover(col)
        return False
    
    if search(0):
        for node in solution:
            r, c, d = map(int, node.name)

            grid[r][c] = d
            screen.fill(white)
            draw.drawGrid(screen, size)
            draw.drawNumbers(screen, grid, size, font)

            pygame.display.flip()

        print("Rest easy, your sudoku has been solved...")
    else: 
        print("No solution found")




#Responsible for displaying the sudoku into a pygame window
def run_sudoku_display(grid):
    screen, font = init_pygame()
    font = pygame.font.SysFont('arial', int(cellSize // 2))
    clock = pygame.time.Clock()
    draw = drawSudoku(cellSize)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d:
                
                    dfs_backtracking_solver(grid, screen, font, draw)
                
                if event.key == pygame.K_l:
                    solve_sudoku_dlx(grid, screen, font, draw)

                if event.key == pygame.K_r:
                    grid = load_sudoku('sudoku.csv')
                    print(grid)
                    run_sudoku_display(grid)

                if event.key == pygame.K_q:
                    running = False
            
        
        
        screen.fill(white)
        draw.drawGrid(screen, size)
        draw.draw_numbers(screen, font, grid)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit() 


if __name__ == "__main__":
    grid = load_sudoku('sudoku.csv')
    print(grid)
    run_sudoku_display(grid)
