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
#from incidence_matrix import *




#CONSTANTS

""" Colors """
white = (255, 255, 255)
black = (0, 0, 0)
size = 540
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

#Solve the sudoku using the dancing links algorithm





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
                    print("Solving using Dancing Links")

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
    #run_sudoku_display(grid)

    #sparse_matrix = IncidenceMatrix(grid)
    


