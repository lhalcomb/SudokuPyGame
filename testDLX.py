from DLX import *

# Example Usage
dlx = DLX()

# Add columns
for name in ["A", "B", "C", "D", "E", "F", "G"]:
    dlx.add_column(name)


# Add rows (each row is a list of column names where there's a 1)
dlx.add_row(["A", "C", "E"])
dlx.add_row(["B", "D", "G"])
dlx.add_row(["A", "D", "F"])
dlx.add_row(["C", "E", "G"])

#print the incidence matrix
for column in dlx.columns.values():
    print(column.name)
    node = column.down
    while node != column:
        print("row      ", node.header.name)
        node = node.down
