class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinaryTree:
    def __init__(self, root=1):
        self.root = root

    def inOrderRecursive(self, root):
        if root is None:
            return "Empty tree"
        else:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

    def inOrderIterative(self, root):
        if root is None:
            print("Empty tree")
            return
        stack = []
        result = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right
