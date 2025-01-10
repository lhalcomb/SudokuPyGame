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


#CONSTANTS

""" Colors """
white = (255, 255, 255)
black = (0, 0, 0)
width = 900; height = 900


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku Solver")
    font = pygame.font.SysFont(None, 40)
    return screen, font

def load_sudoku(file_path) -> list[list[int]]:
    df = pd.read_csv(file_path)
    random_quiz = random.choice(df['quizzes'])
    grid = np.array([int(char) for char in random_quiz]).reshape(9, 9)
    return grid



class drawSudoku:
    def __init__(self, cellSize):
        self.cellSize = cellSize


    def drawGrid(self, screen):
        for i in range(0, 10):
            line_thickness = 3 if i % 3 == 0 else 1
            pygame.draw.line(screen, black, (0, i * self.cellSize), (540, i * self.cellSize), (line_thickness))
            pygame.draw.line(screen, black, (i * self.cellSize, 0), ( i * self.cellSize, 540), (line_thickness))

    def draw_numbers(self, screen, font, grid):
        for row in range(9):
            for col in range(9):
                num = grid[row][col]

                if num != 0:
                    text = font.render(str(num), True, black)
                    text_rect = text.get_rect(center=(col * self.cellSize + self.cellSize // 2, row * self.cellSize + self.cellSize // 2))
                    screen.blit(text, text_rect)

if __name__ == "__main__":
    grid = load_sudoku('sudoku.csv')
    print(grid)

    #Runs the Game Loop
    screen, font = init_pygame()
    clock = pygame.time.Clock()
    draw = drawSudoku(60)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)
        draw.drawGrid(screen)
        draw.draw_numbers(screen, font, grid)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit() 