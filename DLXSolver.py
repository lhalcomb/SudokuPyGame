from incidence_matrix import *


class DLXSolver: 
    def __init__(self, Matrix: IncidenceMatrix):
        self.root = Matrix.header
        self.solutions = []
    
    def solve(self):
        pass

    def choose_column(self):
        pass

    def cover(self, column: Column):
        pass

    def uncover(self, column: Column):
        pass