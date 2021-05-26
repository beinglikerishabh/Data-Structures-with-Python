class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BSTree:
    def __init__(self, root=1):
        self.root = root

    def findMin(self, root):
        if not root:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current

    def findMax(self, root):
        if not root:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current
