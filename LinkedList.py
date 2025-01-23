
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.right = None
        self.left = None
class LinkedList:
    def cover(self, node):
        node.left.right = node.right
        print("After setting node.left.right:", node.left.right.data if node.left.right else None)
        node.right.left = node.left
        print("After setting node.right.left:", node.right.left.data if node.right.left else None)
    def uncover(self, node):
        node.left.right = node
        print("After setting node.left.right:", node.left.right.data if node.left.right else None)
        node.right.left = node
        print("After setting node.right.left:", node.right.left.data if node.right.left else None)

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.right = node2
    node2.left = node1
    node2.right = node3
    node3.left = node2

    print("Before cover:")
    print("node1.right:", node1.right.data if node1.right else None)
    print("node2.left:", node2.left.data if node2.left else None)
    print("node2.right:", node2.right.data if node2.right else None)
    print("node3.left:", node3.left.data if node3.left else None)

    ll = LinkedList()
    ll.cover(node2)

    print("After cover:")
    print("node1.right:", node1.right.data if node1.right else None)
    print("node2.left:", node2.left.data if node2.left else None)
    print("node2.right:", node2.right.data if node2.right else None)
    print("node3.left:", node3.left.data if node3.left else None)
    
    ll.uncover(node2)
    print("After uncover:")
    print("node1.right:", node1.right.data if node1.right else None)
    print("node2.left:", node2.left.data if node2.left else None)
    print("node2.right:", node2.right.data if node2.right else None)
    print("node3.left:", node3.left.data if node3.left else None)