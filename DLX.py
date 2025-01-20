
class Node:
    def __init__(self, name, row = None, col = None):
        
        self.row = row
        self.col = col
        self.left = self.right = self.up = self.down = None
        

class DLX:
    def __init__(self):
        self.head = Node(name="head")
        self.columns = {} #Dictionary to store the columns
        self.nodes = [] #List to store the nodes
    
    def add_node(self, row, col):
        node = Node(name = f"R{row}C{col}")
        self.nodes.append(node)
        #TODO
        pass

    def cover(self, node):
        pass

    def uncover(self, node):
        pass

    def iterate(self, move):
        pass

    

    

