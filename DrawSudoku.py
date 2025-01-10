import pygame 

black = (0, 0, 0)
class drawSudoku:
    def __init__(self, cellSize):
        self.cellSize = cellSize


    def drawGrid(self, screen):
        for i in range(10):
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

