from typing import List
import numpy as np

Matrix2D = List[List[int]]

class Cell:
    def __init__(self, name = None, left = None, right = None, up = None, down = None, col = None):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.col = col
        self.name = name

class Column(Cell):
    def __init__(self, size = 0, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.size = size        

class Root(Column):
    def __init__(self) -> None:
        super().__init__(name = "root")

class IncidenceMatrix: 
    def __init__(self, grid: Matrix2D):
        self.header: Root = Root()
        self.columns: List[Column] = [None] * 324
        self.sudoku_incidence = self.generate_incidence_matrix(grid)
        self.create_dbly_linked_list()
    
    def grid(self) -> Matrix2D:
        return self.grid
    
    def generate_incidence_matrix(self, grid: Matrix2D) -> np.ndarray:
        Matrix2D = np.zeros((729, 324), dtype= int)
        for row in range(9):
            for col in range(9):
                for num in range(9):
                    row_index = num + col * 9 + row * 9 * 9
                    if grid[row][col] != 0 and grid[row][col] - 1 != num:
                        continue

                    #cell constraint
                    Matrix2D[row_index][81 * 0 + col + row * 9] = 1

                    #row constraint
                    Matrix2D[row_index][81 * 1 + num + row * 9] = 1

                    #col constraint
                    Matrix2D[row_index][81 * 2 + num + col * 9] = 1

                    #box constraint
                    box = (row // 3) * 3 + (col // 3)
                    Matrix2D[row_index][81 * 3 + 9 * box + num] = 1
        
        return Matrix2D
    
    
    
    def create_dbly_linked_list(self):
        self.create_columns()
        self.connect_rows()

    def create_columns(self) -> None:
        prev_col = self.header
        for col_index in range(324):
            name = f"col->{col_index}"
            col = Column(size=0, name=name)
            col.left = prev_col
            prev_col.right = col
            self.columns[col_index] = col
            prev_row = col
            for cell_index in range(729):
                if self.sudoku_incidence[cell_index][col_index] != 1:
                    continue
                row = Cell(name=f"row->{cell_index}", col=col)
                col.size += 1
                row.up = prev_row
                prev_row.down = row
                prev_row = row
            col.up = prev_row
            prev_row.down = col
            prev_col = col
        self.header.left = prev_col
        prev_col.right = self.header

    def connect_rows(self) -> None:
        for row in range(729):
            ones_in_row = self.ones_in_row(row)

            if len(ones_in_row) == 0:
                continue

            first_cell = self.get_cell_from_columns(row, ones_in_row[0])
            prev_cell = first_cell

            for col in ones_in_row[1:]:
                cell = self.get_cell_from_columns(row, col)

                cell.left = prev_cell
                prev_cell.right = cell

                prev_cell = cell
            
            first_cell.left = prev_cell
            prev_cell.right = first_cell

    def get_cell_from_columns(self, row_index, col_index) -> Cell | None:
        if self.sudoku_incidence[row_index][col_index] == 0:
            return None
        
        col = self.columns[col_index]

        cell = col.down
        while cell != col:
            if int(cell.name.split('->')[1]) == row_index:
                return cell
            cell = cell.down

        return None

    def ones_in_row(self, row) -> List[int]:
            # ones = []
            
            # for row in range(len(self.grid[0])):
            #     if self.grid[row] == 1:
            #         ones.append(row)
            
            # return ones
            return [col for col in range(324) if self.sudoku_incidence[row][col] == 1]
    def print_sparse_matrix(self): 
        cells: List[List[str]] = [[self.header.name]]
        col = self.header.right

        while col is not self.header:
            row_cells = [col.name]

            row = col.down

            while row is not col:
                row_cells.append(row.name)

                row = row.down
            row_cells.append(f"column size->{str(col.size)}")  #checking col size
            col = col.right
            
            cells.append(row_cells)

        for row in cells:
            print(', '.join(row))


if __name__ == "__main__":
    # grid_noSol = [
    #         [1, 0, 1, 0],
    #         [0, 1, 1, 0],
    #         [0, 0, 1, 0],
    #         [1, 0, 1, 1]]

    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    sparse_matrix = IncidenceMatrix(sudoku_grid)
    sparse_matrix.print_sparse_matrix()

    print("                        \n")
    print("                        \n")

    for col in sparse_matrix.columns:
        print(f"Column Name: {col.name}, Column Size -> {col.size}")
    """This means, for the respective contraint, how many empty cells are there in the column """

    # im = IncidenceMatrix.generate_incidence_matrix()
    # print(np.array(im))
