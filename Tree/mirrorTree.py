class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinaryTree:
    def __init__(self, root=1):
        self.root = root

    def findmirror(self,root):
        if root:
            self.findmirror(root.left)
            self.findmirror(root.right)
            root.left,root.right = root.right,root.left
        return root
