
class Node:
    def __init__(self, name, row, col):
        
        self.row = row
        self.col = col
        self.left = self.right = self.up = self.down = self
        

class DLX:
    def __init__(self):
        self.head = Node(name="head", row=None, col=None)
        self.head.left = self.head
        self.head.right = self.head


        self.columns = {} #Dictionary to store the columns
        self.row_starts = {} #Dictionary to store the row starting
        self.nodes = [] #List to store the nodes

    def add_column(self, col):
        #debugging 
        if col is None:
            raise ValueError("Column cannot be None")
        """Add a column to the DLX Data Structure"""
        if col not in self.columns:

            col_node = Node(name = f"Col: {col}", row = None, col = col)

            #Link the column header node into the circular doubly linked list of columns
            col_node.left = self.head.left
            col_node.right = self.head
            self.head.left.right = col_node
            self.head.left = col_node

            self.columns[col] = col_node
        

    def add_node(self, row, col):
        #debugging 
        if col is None:
            raise ValueError("Column cannot be None")
        """Add a node to the DLX Data Structure"""
        if col not in self.columns:
            self.add_column(col) #Add the column if it does not exist

        col_node = self.columns[col]

        new_node = Node(name = f" R{row}C{col}" , row = row, col = col)
        self.nodes.append(new_node) #here to track the nodes, gonna make a graphical structure later


        #Link vertically in the column 
        new_node.up = col_node.up
        new_node.down = col_node
        col_node.up.down = new_node
        col_node.up = new_node

        #Link horizontally in the row 
        if row not in self.row_starts:
            #first node in the row
            self.row_starts[row] = new_node
            new_node.left = new_node.right = new_node #point back to itself
        else:
            #add to the end of the row
            row_start = self.row_starts[row]
            new_node.left = row_start.left
            new_node.right = row_start
            row_start.left.right = new_node
            row_start.left = new_node
                

    def cover(self, node):
        if node.col is None:
            raise ValueError("Node column cannot be None in cover method")
        """Cover a node in the DLX Data Structure {take it away from the structure}"""
        col_node = self.columns[node.col]
        col_node.left.right = col_node.right
        col_node.right.left = col_node.left

        #Iterate over the column
        for row_node in self.iterate(col_node.down, "down"):
            #Iterate over the row
            for col_node in self.iterate(row_node.right, "right"):
                col_node.up.down = col_node.down
                col_node.down.up = col_node.up

    def uncover(self, node):
        """Uncover a node in the DLX Data Structure {bring it back to the structure}"""
        col_node = self.columns[node.col]
        col_node.left.right = col_node
        col_node.right.left = col_node

        #Iterate over the column
        for row_node in self.iterate(col_node.up, "up"):
            #Iterate over the row
            for col_node in self.iterate(row_node.right, "right"):
                col_node.up.down = col_node
                col_node.down.up = col_node 

    def iterate(self, start, direction):
        """Iterate over the nodes in a circular doubly linked list"""
        node = start
        while True: #while node
            yield node
            node = getattr(node, direction)
            if node == start:
                break
        
        


    

    

