from incidence_matrix import *


class DLXSolver: 
    def __init__(self, Matrix: IncidenceMatrix):
        self.root = Matrix.header
        self.solutions = []
    
    def solve(self):
        if self.root.right == self.root:
            return self.solutions
        
        column = self.choose_column()
        self.cover(column)

        row = column.down 
        while row != column:
            self.solutions.append(row)
            right_node = row.right
            while right_node != row:
                self.cover(right_node.col)
                right_node = right_node.right
            
            result = self.solve()
            if result:
                return result
            
            self.solutions.pop()
            left_node = row.left
            while left_node != row:
                self.uncover(left_node.col)
                left_node = left_node.left
            
            row = row.down
        
        self.uncover(column)
        return None

    def choose_column(self) -> Column:
        col = self.root.right
        min_col = col
        min_size = col.size

        while col != self.root:
            if col.size < min_size:
                min_col = col
                min_size = col.size
            col = col.right

        return min_col

    def cover(self, column: Column):
        column.right.left = column.left
        column.left.right = column.right

        row = column.down
        while row != column:
            cell = row.right
            while cell != row:
                cell.down.up = cell.up
                cell.up.down = cell.down
                cell.col.size -= 1
                cell = cell.right
            row = row.down

    def uncover(self, column: Column):
        node = column.up
        while node != column:
            cell = node.left
            while cell != node:
                cell.col.size += 1
                cell.down.up = cell
                cell.up.down = cell
                cell = cell.left
            node = node.up
        column.right.left = column
        column.left.right = column
