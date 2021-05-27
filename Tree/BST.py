class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BSTree:
    def __init__(self, root=1):
        self.root = root

    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.data > node.data:
                if root.left is None:
                    root = node
                else:
                    self.insert(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)

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

    def findDataRecursive(self, root, data):
        current = root
        while current is not None and current.data != data:
            if data > current.data:
                current = current.right
            else:
                current = current.left
