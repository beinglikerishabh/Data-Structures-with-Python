class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinaryTree:
    def __init__(self, root=1):
        self.root = root

    def size(self,root):
        if not root:
            return 0
        return (self.size(root.left) + self.size(root.right)+1)