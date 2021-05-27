import Queue.queuewithLL as Queue


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinaryTree:
    def __init__(self, root=1):
        self.root = root

    def levelOrder(self,root):
        if root is None:
            return "Empty treee"
        result = []
        q = Queue.Queue()
        q.EnQueue(root)
        node = None
        while not q.isEmpty():
            node = q.DeQueue()
            result.append(node.data)
            if node.left is not None:
                q.EnQueue(node.left)
            if node.right is not None:
                q.EnQueue(node.right)

#create a queue and run or get the driver code from gfg
        


