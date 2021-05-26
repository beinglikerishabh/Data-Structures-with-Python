class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinaryTree:
    def __init__(self, root=1):
        self.root = root

    def postOrderRecursive(self,root):
        if root is None:
            return "nothing in the Tree"
        self.postOrderRecursive(root.left)
        self.postOrderRecursive(root.right)
        print(root.data,end=" ")
    
    def postOrderIterative(self,root):
        if root is None:
            return "tree is empty"
        result = []
        visited = set()
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.data)
                    node = None



        
        