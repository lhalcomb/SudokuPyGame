
class RowNode:
    def __init__(self, ):
        self.left = self  # Left link
        self.right = self  # Right link
        self.up = self  # Up link
        self.down = self  # Down link
        self.header = None  # Pointer to the column header this node belongs to
      
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
       self.columns = {} 


    def add_column(self, name):
        """Add a column to the DLX Data Structure"""
        column = ColumnHeader(name=name)
        self.columns[name] = column
        
        # Link the column to the root
        last = self.root.left
        last.right = column
        column.left = last
        column.right = self.root
        self.root.left = column

        

    def add_row(self, row):
        """Add a row to the incidence matrix"""
        first_node = None
        prev_node = None
        for column_name in row:
            column = self.columns[column_name]
            node = RowNode()
            node.header = column
            column.increment_size()

           # Link vertically in the column
            last = column.up
            last.down = node
            node.up = last
            node.down = column
            column.up = node

            # Link horizontally in the row
            if first_node is None:
                first_node = node
            else:
                previous_node.right = node
                node.left = previous_node

            previous_node = node

        # Complete the circular row linkage
        if first_node is not None:
            previous_node.right = first_node
            first_node.left = previous_node

    def cover(self, node):
        """Cover a node in the DLX Data Structure {take it away from the structure}"""
        pass

    def uncover(self, node):
        """Uncover a node in the DLX Data Structure {bring it back to the structure}"""
        pass

    def iterate(self, start, direction):
        """Iterate over the nodes in a circular doubly linked list"""
        pass
        
        


    

    

