import pygame 

black = (0, 0, 0)
hack_green = (43, 83, 41)
background_green = (100, 149, 104)

class drawSudoku:
    def __init__(self, cellSize):
        self.cellSize = cellSize
        


    def drawGrid(self, screen, size):
        for i in range(10):
            line_thickness = 3 if i % 3 == 0 else 1
            pygame.draw.line(screen, hack_green, (0, i * self.cellSize), (size, i * self.cellSize), (line_thickness)) #horizontal line
            pygame.draw.line(screen, hack_green, (i * self.cellSize, 0), ( i * self.cellSize, size), (line_thickness)) #vertical line

    def draw_numbers(self, screen, font, grid):
        for row in range(9):
            for col in range(9):
                num = grid[row][col]

                if num != 0:
                    text = font.render(str(num), True, background_green)
                    text_rect = text.get_rect(center=(col * self.cellSize + self.cellSize // 2, row * self.cellSize + self.cellSize // 2))
                    screen.blit(text, text_rect)

