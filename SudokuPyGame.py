"""
Sudoku Project built in pygame for algorithms to solve sudoku puzzles

Algorithms Used:
- Backtracking Algorithms: DFS, Dancing Links

"""

import pygame

pygame.init()
width = 900; height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Solver")
clock = pygame.time.Clock()

class drawSudoku:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    screen.fill("white")


    pygame.display.flip()

    clock.tick(60)  

pygame.quit()