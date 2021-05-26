class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinaryTree:
    def __init__(self, root=1):
        self.root = root

    def preOrderRecursive(self, root):
        if root == None:
            return
        print(root.data)
        self.preOrderRecursive(root.left)
        self.preOrderRecursive(root.right)

    # need to use stack so that backtrack the node if no further element deep
    def preOrderIterative(self, root):
        if not root:
            return "no element"
        result = []
        stack = []
        stack.append(root)  # append root at the very first to pop at first
        while stack:  # will run untill stack epmty
            node = stack.pop()
            result.append(node.data)
            if node.right:  # append right  first so that popped after left
                stack.append(node.right)
            if node.left:   # append left at last so that popped at first
                stack.append(node.left)
        return result
