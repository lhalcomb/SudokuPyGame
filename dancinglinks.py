import pygame
from incidence_matrix import *
from SudokuPyGame import load_sudoku
from DLXSolver import *

def solve_sudoku_dancing_links(grid):
    matrix = IncidenceMatrix(grid)
    solver = DLXSolver(matrix)  
    solutions = solver.solve()

    return solutions

def init_pygame():
    pygame.init()

    screen = pygame.display.set_mode((2160, 2160))
    pygame.display.set_caption("Dancing Links Incidence Matrix")

    return screen

def draw_matrix(screen, matrix, node_size):
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            if matrix[row][col] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (row * node_size, col * node_size, node_size, node_size))

def draw_connections(screen, matrix, cell_size):
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 1:
                x = j * cell_size + cell_size // 2
                y = i * cell_size + cell_size // 2
                if i > 0 and matrix[i - 1, j] == 1:  # Up
                    pygame.draw.line(screen, (255, 0, 0), (x, y), (x, y - cell_size))
                if i < matrix.shape[0] - 1 and matrix[i + 1, j] == 1:  # Down
                    pygame.draw.line(screen, (255, 0, 0), (x, y), (x, y + cell_size))
                if j > 0 and matrix[i, j - 1] == 1:  # Left
                    pygame.draw.line(screen, (255, 0, 0), (x, y), (x - cell_size, y))
                if j < matrix.shape[1] - 1 and matrix[i, j + 1] == 1:  # Right
                    pygame.draw.line(screen, (255, 0, 0), (x, y), (x + cell_size, y))

def main():
    screen = init_pygame()
    node_size = 5
    sudoku_grid = load_sudoku("sudoku.csv")
    matrix = IncidenceMatrix(sudoku_grid)
    solver = DLXSolver(matrix)
   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_l:
                        print("Solving using Dancing Links...")
                        #solutions = solve_sudoku_dancing_links(sudoku_grid)
                        solutions = solver.solve()

                        if solutions:
                            for row_node in solutions:
                                row, col, num = int(row_node.name.split('->')[1]) // 81, (int(row_node.name.split('->')[1]) % 81) // 9 , int(row_node.name.split('->')[1]) % 9
                                sudoku_grid[row][col] = num + 1
                                print(f"Row: {row} Col: {col} Num: {num + 1}")
                                
                                solver.cover(row_node.col)
                                screen.fill((0, 0, 0))
                                draw_matrix(screen, matrix.sudoku_incidence, node_size)
                                draw_connections(screen, matrix.sudoku_incidence, node_size)
                                pygame.display.flip()
                                pygame.time.delay(1)
                        else:
                            print("No Solution Found")

        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
     # grid_noSol = [
    #         [1, 0, 1, 0],
    #         [0, 1, 1, 0],
    #         [0, 0, 1, 0],
    #         [1, 0, 1, 1]]


    sudoku_grid = load_sudoku("sudoku.csv")
    print(sudoku_grid)
    # sudoku_grid = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ]
    
    sparse_matrix = IncidenceMatrix(sudoku_grid)
    sparse_matrix.print_sparse_matrix()

    print("                        \n")
    print("                        \n")

    for col in sparse_matrix.columns:
        print(f"Column Name: {col.name}, Column Size -> {col.size}")
    """This means, for the respective contraint, how many empty cells are there in the column """

    # im = IncidenceMatrix.generate_incidence_matrix()
    # print(np.array(im))
    #num_rows, num_cols = sparse_matrix.sudoku_incidence.shape
    # num_rows = sparse_matrix.shape()[0]
    # print(num_rows)
    # print((sparse_matrix.sudoku_incidence[1][0].size))

    main()