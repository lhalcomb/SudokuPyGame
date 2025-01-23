
class Node:
    def __init__(self, name, row, col):
        
        self.name = name
        self.row = row
        self.col = col
        self.up = None
        self.down = None
        self.left = None
        self.right = None


class DLX:
    def __init__(self, header):
       self.header = header


    def add_column(self, col):
       pass
        

    def add_node(self, row, col):
        pass

    def cover(self, node):
        """Cover a node in the DLX Data Structure {take it away from the structure}"""
        pass

    def uncover(self, node):
        """Uncover a node in the DLX Data Structure {bring it back to the structure}"""
        pass

    def iterate(self, start, direction):
        """Iterate over the nodes in a circular doubly linked list"""
        pass
        
        


    

    

