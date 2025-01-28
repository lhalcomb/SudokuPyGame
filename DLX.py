
class RowNode:
    def __init__(self, ):
        self.left = self  # Left link
        self.right = self  # Right link
        self.up = self  # Up link
        self.down = self  # Down link
        
      
class ColumnHeader(RowNode):
    def __init__(self, name = None):
        super().__init__()
        self.size = 0
        self.name = name

    def increment_size(self):
        self.size += 1

    def decrement_size(self):
        self.size -= 1


class DLX:
    def __init__(self):
       self.root = ColumnHeader(name="root")


    def add_column(self, name):
        """Add a column to the DLX Data Structure"""
        

    def add_row(self, row):
        """Add a row to the incidence matrix"""
        

    def cover(self, node):
        """Cover a node in the DLX Data Structure {take it away from the structure}"""
        pass

    def uncover(self, node):
        """Uncover a node in the DLX Data Structure {bring it back to the structure}"""
        pass

    def iterate(self, start, direction):
        """Iterate over the nodes in a circular doubly linked list"""
        pass
        
        


    

    

