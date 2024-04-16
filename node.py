class Node:
    """
    node of formula in tree representation
    """

    def __init__(self, t):
        self.satisfying_states = set()
        self.node_count = 0
        self.t = t
        self.type = t[0]
        self.length = len(t)
        self.child = None
        self.left = None
        self.right = None
        if self.length == 2:
            self.child = Node(t[1]) if isinstance(t[1], (tuple)) else t[1]

        elif self.length == 3:
            self.left = Node(t[1]) if isinstance(t[1], (tuple)) else t[1]
            self.right = Node(t[2]) if isinstance(t[2], (tuple)) else t[2]
        self.set_node_count()

    def set_node_count(self):
        """
        count no of nodes in the descendent trees and set in node_count
        """
        if self.length == 2:
            self.node_count = 1 + (
                self.child.node_count
                if isinstance(self.child, Node)
                else (1 if isinstance(self.child, str) else 0)
            )
        else:
            self.node_count = (
                1
                + (
                    self.left.node_count
                    if isinstance(self.left, Node)
                    else (1 if isinstance(self.left, str) else 0)
                )
                + (
                    self.right.node_count
                    if isinstance(self.right, Node)
                    else (1 if isinstance(self.right, str) else 0)
                )
            )

    def inorder_traversal(self):
        """
        given a node, print its inorder traversal
        a node's child/left/right could be node or string.
        """
        print(self.type, self.t)
        if self.length == 2:

            if isinstance(self.child, Node):
                self.child.inorder_traversal()

            elif self.child is not None:
                print(self.child)

        else:

            if isinstance(self.left, Node):
                self.left.inorder_traversal()
            elif self.left is not None:
                print(self.left)

            if isinstance(self.right, Node):
                self.right.inorder_traversal()
            elif self.right is not None:
                print(self.right)


p = Node(("not", ("EU", ("T",), ("NOT", ("VAR", "f")))))
print("Inorder Traversal")
p.inorder_traversal()
print(p.node_count)
