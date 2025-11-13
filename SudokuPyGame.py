"""
Sudoku Project built in pygame for algorithms to solve sudoku puzzles

Algorithms Used:
- Backtracking Algorithms: DFS, Dancing Links

"""

import os
import pygame
import pandas as pd
import numpy as np
import sys
import time
import random
from DrawSudoku import drawSudoku
from DLXSolver import *




#CONSTANTS

""" Colors """
white = (255, 255, 255)
black = (0, 0, 0)
hack_green = (43, 83, 41)
back_ground_green = (100, 149, 104)
light_green = (144, 238, 144)

size = 600
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
    if (file_path == 'sudoku9.csv'):
        random_quiz = random.choice(df['puzzle'])
    else:
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
                        screen.fill(black)
                        draw.drawGrid(screen, size)
                        draw.draw_numbers(screen, font, grid)
                        pygame.display.flip()
                        if dfs_backtracking_solver(grid, screen, font, draw):
                            return True
                        grid[row][col] = 0
                        screen.fill(black)
                        draw.drawGrid(screen,size)
                        draw.draw_numbers(screen, font, grid)
                        pygame.display.flip()

                return False
    return True


"""Dancing Links Implementation"""

#Solve the sudoku using the dancing links algorithm

def solve_sudoku_dancing_links(grid): 
    matrix = IncidenceMatrix(grid)
    solver = DLXSolver(matrix)  
    solutions = solver.solve()

    return solutions

def solve_sudokucsv(file_path):
    df = pd.read_csv(file_path)
    solve_count = 0 
    total_solve_time = 0

    iteration_file = '/benchmarking/iteration_count.txt'
    if os.path.exists(iteration_file):
        with open(iteration_file, 'r') as f:
            iteration_count = int(f.read().strip())
    else:
        iteration_count = 0

    iteration_count += 1

    for index, row in df.iterrows():
        grid = np.array([int(char) for char in row['quizzes']]).reshape(9, 9)
        matrix = IncidenceMatrix(grid)
        solver = DLXSolver(matrix)  

        start_time = time.time()
        solutions = solver.solve()
        end_time = time.time()
        solve_time = end_time - start_time

        total_solve_time += solve_time

        if solutions:
            solve_count += 1
            for row_node in solutions:
                row, col, num = int(row_node.name.split('->')[1]) // 81, (int(row_node.name.split('->')[1]) % 81) // 9 , int(row_node.name.split('->')[1]) % 9 
                grid[row][col] = num + 1

            if solve_count % 10000 == 0:
                print_grid(grid, solve_count, solve_time)
            print_grid(grid, solve_count, solve_time)
        
        else:
            print("No Solution Found")
    
    if solve_count > 0:
        average_solve_time = total_solve_time / solve_count
    else: 
        average_solve_time = 0
    
    print(f"Average Solve Time: {average_solve_time:.4f} seconds")

    with open('/benchmarking/average_solve_time.txt', 'w') as f:
        f.write(f"Iteration: {iteration_count} Average Solve Time: {average_solve_time:.4f} seconds")
    
    with open(iteration_file, 'w') as f:
        f.write(str(iteration_count))

        
def print_grid(grid, solve_count, solve_time):
    print(f"Grid Solution: {solve_count}")
    print(f"Solved in: {solve_time:.4f} seconds")
    for row in grid:
        print(" ".join(str(num) for num in row))
    print("\n")


#Responsible for displaying the sudoku into a pygame window
def run_sudoku_display(grid):
    screen, font = init_pygame()
    font = pygame.font.SysFont('arial', int(cellSize // 2))
    clock = pygame.time.Clock()
    draw = drawSudoku(cellSize)

    current_step = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d:
                
                    dfs_backtracking_solver(grid, screen, font, draw)
                
                if event.key == pygame.K_l:
                    print("Solving using Dancing Links...")
                    matrix = IncidenceMatrix(grid)
                    solver = DLXSolver(matrix)  
                    solutions = solver.solve()

                    if solutions:
                        for row_node in solutions:
                            row, col, num = int(row_node.name.split('->')[1]) // 81, (int(row_node.name.split('->')[1]) % 81) // 9 , int(row_node.name.split('->')[1]) % 9 
                            grid[row][col] = num + 1

                        screen.fill(black)
                        draw.drawGrid(screen, size)
                        draw.draw_numbers(screen, font, grid)

                        
                        
                        pygame.display.flip()
                    else:
                        print("No Solution Found")

                    
                    
                    grid = load_sudoku('sudoku9.csv')
                    run_sudoku_display(grid)
                
                if event.key == pygame.K_x:
                    print("Solving using Dancing Links...")
                    matrix = IncidenceMatrix(grid)
                    solver = DLXSolver(matrix)  
                    solutions = solver.solve()


                    if solutions: 
                        for row_node in solutions:
                            row, col, num = int(row_node.name.split('->')[1]) // 81, (int(row_node.name.split('->')[1]) % 81) // 9 , int(row_node.name.split('->')[1]) % 9 
                            grid[row][col] = num + 1

                            screen.fill(black)
                            draw.drawGrid(screen, size)
                            draw.draw_numbers(screen, font, grid)
                            pygame.display.flip()
                            clock.tick(30)

                    
                        # text_surface = font.render("Sudoku Solved!!", True, light_green, black)
                        # text_rect = text_surface.get_rect(center=(size // 2, size // 2))
                        # screen.blit(text_surface, text_rect)
                        pygame.display.flip()

                        # waiting = True
                        # while waiting:
                        #     for event in pygame.event.get():
                        #         if event.type == pygame.KEYDOWN:
                        #             waiting = False

                   
                
                if event.key == pygame.K_SPACE:
                    solutions = solve_sudoku_dancing_links(grid)
                    for row_node in solutions:
                        row, col, num = int(row_node.name.split('->')[1]) // 81, (int(row_node.name.split('->')[1]) % 81) // 9 , int(row_node.name.split('->')[1]) % 9
                        grid[row][col] = num + 1
                        current_step += 1
                        print(f"Row: {row} Col: {col} Num: {num + 1}")
                    
                
                    if solutions and current_step < len(solutions):
                        
                        screen.fill(black)
                        draw.drawGrid(screen, size)
                        draw.draw_numbers(screen, font, grid)
                        pygame.display.flip()
                        clock.tick(30)

                if event.key == pygame.K_a:
                    solve_sudokucsv('sudoku9.csv')

                if event.key == pygame.K_r:
                    grid = load_sudoku('sudoku9.csv')
                    print(grid)
                    run_sudoku_display(grid)

                if event.key == pygame.K_q:
                    running = False
            
        
        
        screen.fill(black)
        draw.drawGrid(screen, size)
        draw.draw_numbers(screen, font, grid)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit() 


if __name__ == "__main__":
    #grid = load_sudoku('sudoku9.csv')
    grid1 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 1, 0, 0, 3, 0],
    [0, 0, 6, 0, 2, 0, 7, 0, 0],
    [0, 0, 0, 3, 0, 4, 0, 0, 0],
    [2, 1, 0, 0, 0, 0, 0, 9, 8],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 2, 5, 0, 6, 4, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]).reshape(9,9)
    
    impossible_grid = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                [0, 0, 0, 0, 0, 3, 0, 8, 5], 
                                [0, 0, 1, 0, 2, 0, 0, 0, 0], 
                                [0, 0, 0, 5, 0, 7, 0, 0, 0], 
                                [0, 0, 4, 0, 0, 0, 1, 0, 0], 
                                [0, 9, 0, 0, 0, 0, 0, 0, 0], 
                                [5, 0, 0, 0, 0, 0, 0, 7, 3], 
                                [0, 0, 2, 0, 1, 0, 0, 0, 0], 
                                [0, 0, 0, 0, 4, 0, 0, 0, 9]
                                ]).reshape(9, 9)
    


    #print(grid)
    run_sudoku_display(impossible_grid)
    #run_sudoku_display(grid)
    #solve_sudokucsv('sudoku.csv')
    #sparse_matrix = IncidenceMatrix(grid)
    


