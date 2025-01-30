

class Cell:
    def __init__(sellf, self, left = None, right = None, up = None, down = None, col = None):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.col = col

    def __repr__(self) -> str:
        return f'Cell({self.name}, left = {self.left}, right = {self.right}, up = {self.up}, down = {self.down}, colHeader = {self.col})'
        
    def __str__(self) -> str:
        return self.name

class ColumnHeader(Cell):
    def __init__(self, name, size = 0, *args, **kwargs) -> None:
        super().__init__(name, *args, **kwargs)
        self.size = size        

class Root(ColumnHeader):
    def __init__(self) -> None:
        super().__init__(name = "root")