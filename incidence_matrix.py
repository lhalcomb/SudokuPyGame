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
        self.grid = grid
        self.sudoku_incidence = IncidenceMatrix.generate_incidence_matrix()
        self.create_dbly_linked_list()
    
    def grid(self) -> Matrix2D:
        return self.grid
    
    def generate_incidence_matrix() -> np.ndarray:
        Matrix2D = np.zeros((729, 324), dtype= int)
        for row in range(9):
            for col in range(9):
                for num in range(9):
                    row_index = num + col * 9 + row * 9 * 9

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
        for col_index in range(len(self.grid[0])):
            name = f"col->{col_index}"
            col = Column(size=0, name=name)
            col.left = prev_col
            prev_col.right = col
            prev_row = col
            for cell_index in range(len(self.grid)):
                if self.grid[cell_index][col_index] != 1:
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
        for row in range(len(self.grid)):
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
        if self.grid[row_index][col_index] == 0:
            return None
        
        col = self.header

        while col.name != f"col->{col_index}":
            col = col.right

        cell = col

        while cell.name != f"row->{row_index}":
            cell = cell.down

        return cell

    def ones_in_row(self, row) -> int:
            ones = []
            
            for row in range(len(self.grid[0])):
                if self.grid[row] == 1:
                    ones.append(row)
            
            return ones
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
    grid_noSol = [
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 1, 1]]
    
    sparse_matrix = IncidenceMatrix(grid_noSol)
    sparse_matrix.print_sparse_matrix()

    im = IncidenceMatrix.generate_incidence_matrix()
    print(np.array(im))
